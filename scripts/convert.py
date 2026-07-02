#!/usr/bin/env python3
"""Convert a documentation package (Markdown) into DOCX, PDF, HTML, or PPTX.

Wraps pandoc. Give it a single Markdown file or a directory produced by the
publishing skill; a directory is concatenated in reading order before
conversion so the artifact reads as one document.

Examples:
    python3 scripts/convert.py docs/ --to docx -o product-docs.docx --title "Product Documentation" --toc
    python3 scripts/convert.py docs/overview.md --to pdf -o overview.pdf
    python3 scripts/convert.py docs/ --to html -o docs.html --toc
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Reading order for a standard documentation package. Files not listed here
# are appended alphabetically after the known ones.
DEFAULT_ORDER = [
    "README.md",
    "overview.md",
    "getting-started.md",
    "concepts.md",
    "architecture.md",
    "configuration.md",
    "api-reference.md",
    "examples.md",
    "troubleshooting.md",
    "faq.md",
    "glossary.md",
]

FORMATS = {
    "docx": "docx",
    "pdf": "pdf",
    "html": "html",
    "pptx": "pptx",
    "rst": "rst",
    "asciidoc": "asciidoc",
    "mediawiki": "mediawiki",
    "txt": "plain",
}


def collect_sources(path: Path, order: list[str]) -> list[Path]:
    if path.is_file():
        return [path]
    files = {p.name: p for p in sorted(path.glob("*.md"))}
    ordered = [files.pop(name) for name in order if name in files]
    return ordered + list(files.values())


def concatenate(sources: list[Path], dest: Path) -> None:
    parts = []
    for src in sources:
        text = src.read_text(encoding="utf-8").strip()
        parts.append(text)
    # Page break between documents in formats that honour it (docx/pdf).
    separator = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
    dest.write_text(separator.join(parts) + "\n", encoding="utf-8")


def build_command(source: Path, args: argparse.Namespace, resource_dirs: list[Path]) -> list[str]:
    cmd = [
        "pandoc",
        str(source),
        "--from", "markdown+smart",
        "--output", str(args.output),
        "--resource-path", ":".join(str(d) for d in resource_dirs) or ".",
    ]
    # For PDF, let pandoc infer the writer from the .pdf extension — older
    # releases reject an explicit `--to pdf`.
    if args.to != "pdf":
        cmd += ["--to", FORMATS[args.to]]
    if args.toc:
        cmd += ["--toc", "--toc-depth", "3"]
    if args.title:
        cmd += ["--metadata", f"title={args.title}"]
    if args.date:
        cmd += ["--metadata", f"date={args.date}"]
    if args.number_sections:
        cmd.append("--number-sections")
    if args.reference_doc and args.to == "docx":
        cmd += ["--reference-doc", args.reference_doc]
    if args.to == "html":
        cmd += ["--standalone", "--embed-resources"]
    if args.to == "pdf":
        cmd += ["--variable", "geometry:margin=2.5cm", "--variable", "colorlinks=true"]
        if args.pdf_engine:
            cmd += ["--pdf-engine", args.pdf_engine]
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="Markdown file or directory containing the documentation package")
    parser.add_argument("--to", required=True, choices=sorted(FORMATS), help="Target format")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output file path")
    parser.add_argument("--title", help="Document title (rendered as a title page in DOCX/PDF)")
    parser.add_argument("--date", help="Date shown on the title page")
    parser.add_argument("--toc", action="store_true", help="Insert an automatic table of contents")
    parser.add_argument("--number-sections", action="store_true", help="Number headings")
    parser.add_argument("--order", nargs="*", default=DEFAULT_ORDER, metavar="FILE",
                        help="File reading order when source is a directory (default: standard package order)")
    parser.add_argument("--reference-doc", help="Custom .docx used as a style reference (DOCX only)")
    parser.add_argument("--pdf-engine", help="PDF engine to pass to pandoc (e.g. tectonic, wkhtmltopdf)")
    args = parser.parse_args()

    if shutil.which("pandoc") is None:
        print("error: pandoc is not installed. Install it (e.g. `brew install pandoc`) or use a "
              "document-generation fallback as described in output-formats/SKILL.md.", file=sys.stderr)
        return 1

    if not args.source.exists():
        print(f"error: source not found: {args.source}", file=sys.stderr)
        return 1

    sources = collect_sources(args.source, args.order)
    if not sources:
        print(f"error: no Markdown files found in {args.source}", file=sys.stderr)
        return 1

    base_dir = args.source if args.source.is_dir() else args.source.parent
    resource_dirs = [base_dir, base_dir / "assets"]

    with tempfile.TemporaryDirectory() as tmp:
        merged = Path(tmp) / "merged.md"
        if len(sources) == 1:
            merged = sources[0]
        else:
            concatenate(sources, merged)
        cmd = build_command(merged, args, resource_dirs)
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print("error: pandoc failed — see the message above.", file=sys.stderr)
            return result.returncode

    size_kb = args.output.stat().st_size / 1024
    print(f"wrote {args.output} ({size_kb:.0f} KB) from {len(sources)} file(s)")
    print("Open the file and verify: TOC resolves, headings styled, images present, tables fit the page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
