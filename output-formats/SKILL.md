---
name: output-formats
description: Delivers the finished documentation in the format the user asks for — Markdown, Word (DOCX), PDF, HTML, or a slide deck — including screenshots and diagrams embedded as images where the format supports them.
---

# Output Formats Skill

## Purpose

Markdown is the framework's working format, not its only deliverable. Whatever the user asks for is what they get. If the request says "give it to me as a Word file", the final artifact is a `.docx` on disk, opened and verified — not a Markdown file with a note saying it could be converted.

## Deciding the target format

Follow this order:

1. An explicit request wins: "as PDF", "in Word", "docx olarak", "export to Confluence".
2. Wording that implies a format: "I need to print this" suggests PDF; "I'll paste it into our wiki" suggests HTML or the wiki's markup; "my manager will edit it" suggests DOCX.
3. No signal at all: deliver Markdown and mention, once, that other formats are available on request.

When the user names a format the environment cannot produce, say so plainly and offer the nearest alternative. Do not silently substitute.

## Supported targets

| Target | Produced with | Notes |
|---|---|---|
| Markdown | Direct output | Default. One file per document, per the publishing skill. |
| DOCX (Word) | `scripts/convert.py` (pandoc) or python-docx | Include a title page, table of contents, heading styles, and page numbers. |
| PDF | `scripts/convert.py` (pandoc + a PDF engine), or DOCX → PDF export | If no PDF engine exists, produce DOCX and convert with LibreOffice (`soffice --convert-to pdf`) or Word itself. |
| HTML | `scripts/convert.py` (pandoc, standalone) | Single self-contained file with embedded CSS; images inlined or shipped alongside. |
| Slide deck (PPTX) | pandoc or python-pptx | Only when the user asks for slides; condense, do not paste document prose onto slides. |
| Plain text / RST / AsciiDoc / MediaWiki | pandoc | Available on request. |

## Conversion workflow

1. Finish the documentation in Markdown first and pass technical review. Never convert an unreviewed draft.
2. Keep all referenced images in an `assets/` directory next to the Markdown files, and reference them with relative paths. Pandoc embeds them automatically.
3. Run the converter:

   ```bash
   python3 scripts/convert.py docs/ --to docx --output product-documentation.docx --title "Product Documentation" --toc
   ```

   The script concatenates the package in reading order, applies a clean reference style, and writes the artifact. Run `python3 scripts/convert.py --help` for the full option list.
4. Open or inspect the result before handing it over. For DOCX, confirm at minimum: the TOC resolves, headings use real heading styles (so Word's navigation pane works), tables fit the page, images are visible, and code blocks kept a monospaced font.

If pandoc is not installed and cannot be installed, fall back in this order: a document-generation skill available in the session (for example a dedicated DOCX skill), then python-docx directly. The formatting requirements stay the same regardless of the tool.

## Screenshots and other images

Some documentation needs pictures: a settings screen, a dashboard, terminal output, an architecture diagram. When the user asks for screenshots in the document — or the content clearly needs them — capture and embed rather than describing the image in words.

- **Live UI**: capture with whatever the environment offers — browser preview tooling, a connected browser, or the OS screenshot command (`screencapture` on macOS). Crop to the relevant region; a full 4K desktop shrunk into a page is unreadable.
- **Terminal output**: prefer a fenced code block. Use an image only when the user explicitly wants a screenshot or when color/layout is the point.
- **Diagrams**: author in Mermaid or Graphviz inside the Markdown. For formats that cannot render them (DOCX, PDF), render to PNG or SVG first (`mmdc` for Mermaid, `dot -Tpng` for Graphviz) and embed the image; keep the source text in the repository next to it.

File conventions: store captures as `assets/NN-short-description.png`, numbered in document order. Every image gets a caption and is referenced from the text ("Figure 3 shows the retry queue after a failed delivery") — an image the text never mentions gets deleted.

## Visual design

Formatted deliverables (DOCX, PDF) follow `rules/document-design-rules.md` in full. The short version: research the owning company's official brand palette before styling anything and map it to fixed roles (headings, accents, callouts); build the complete document anatomy (branded cover with metadata table, TOC field, part dividers for long documents, numbered chapters, header/footer); convert enumerable prose to branded tables and callout boxes; renumber figures in reading order and generate a figure index appendix; then validate the OOXML schema, render sample pages to images and inspect them, and — when redesigning an existing document — run a content-loss probe against the source.

## Format-specific quality bar

**DOCX**
- Everything in `rules/document-design-rules.md`, including its §7 self-check.
- Title page: document title, product name, version or date. No author block unless the user provides one.
- Automatic table of contents after the title page.
- Native heading styles (Heading 1–4), not bold body text pretending to be headings.
- Page numbers in the footer.
- Tables with header rows repeated across page breaks when long.

**PDF**
- Same structure as DOCX. Check that no table or code block bleeds off the page edge.

**HTML**
- Standalone file, embedded CSS, working in-page anchors for the TOC.
- Readable without horizontal scrolling at typical window widths; code blocks scroll internally.

**Any format**
- The converted artifact is checked, not assumed. A conversion that ran without errors can still produce a broken TOC or a missing image.
- Deliver the source Markdown alongside the converted file unless the user says otherwise — it is what they will edit next time.
