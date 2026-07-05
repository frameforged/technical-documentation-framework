# Document Design Rules

These rules govern the visual design of formatted deliverables (DOCX, PDF, and by extension HTML and slides). They exist because a technically correct document with default styling reads as a draft, while the same content with deliberate typography, brand color, and structural design reads as a product. Apply them in Phase 10 (output-formats), and earlier in Phase 5 (document-architecture) when planning tables, figures, and callouts.

The standard these rules encode: **the design must be professional, must make the content more visible rather than merely decorated, and must belong to the company the document is written for.**

## 1. Brand research comes before any styling decision

Never invent a color scheme when the document belongs to an identifiable company or product.

1. Identify the owning company or brand from the content or from the user.
2. Search for the official corporate identity guide ("brand guidelines", "kurumsal kimlik kılavuzu"). Companies usually publish these as PDFs on their own domain. Extract the primary and secondary palette as HEX values, and the corporate typeface if one is named.
3. Record where each color came from (guide page, URL) so the choice is defensible.
4. If no official guide exists, extract dominant colors from the company's logo or website, and say so.
5. If the brand cannot be identified at all, ask the user once; if there is no answer, fall back to a restrained neutral scheme (one dark tone for headings and one accent) — never a rainbow of arbitrary colors.

Map the palette to roles, and use it consistently:

| Role | Use | Typical source |
|---|---|---|
| Primary dark | H1/H2 headings, table header rows, cover title, page-number emphasis | Brand's dark corporate color |
| Accent | Rules under headings, cover subtitle, bullet glyphs, code-block edge bar, quote bars | Brand's bright corporate color |
| Alternates (2–4) | Callout boxes by semantic (warning, tip, info), status colors | Brand's alternative palette |
| Neutrals | Body text (near-black, not pure black), captions and metadata (mid gray), zebra rows and code backgrounds (very light tint) | Derived |

Corporate typefaces are often not installed on the reader's machine. Use a universally available family (Calibri, Arial) for the document body and note the substitution; do not embed a font you cannot license.

## 2. Document anatomy

A formatted deliverable of manual or product-documentation length has all of the following, in order:

1. **Cover page.** Company wordmark (text is fine — letter-spaced, in a neutral tone, over an accent rule), product name large in primary dark, document type as subtitle in accent, a one-line tagline, and a compact metadata table (document type, covered product version, SDK/API version, date, language note). The cover carries no header, footer, or page number — use a separate section for it. Verify the metadata table does not spill to page 2.
2. **Table of contents** as a real TOC field over native heading styles (levels 1–2), so Word's navigation pane and the TOC both work. Tell the user the field needs one "Update Field" in Word; a field TOC renders as a placeholder in preview converters and that is expected.
3. **Part divider pages** when the document has roughly ten or more chapters. Group chapters into named parts (e.g. Overview → Usage → Extending → Governance → Reference), each divider carrying the part label, part title, an accent rule, and a one-or-two-sentence italic description of what the part covers and who needs it. Dividers use a display style, not Heading styles, so they stay out of the TOC.
4. **Numbered chapters.** H1 = `1. Title` starting on a fresh page with a thick accent rule beneath; H2 = `1.1 Title`. Leave H3 unnumbered when the content already numbers itself (wizard steps, phases). Heading styles must be the built-in Heading 1–3 with overridden fonts/colors — never bold body text — or the TOC and navigation break.
5. **Header and footer** on every content page: a small italic document title in the header over a thin accent rule, and a footer with company · product on the left and the page number right-aligned via a tab stop. Never build header/footer dividers out of tables.
6. **Appendices** for generated indexes — at minimum a figure index (see §4).

## 3. Make information visible: tables, callouts, code

Design is not decoration; it is turning buried prose into structures the eye can scan.

- **Prose that enumerates becomes a table.** Problem→solution mappings, role/permission matrices, menu maps, comparison of options, embedding-model choices, glossaries. Table style: header row filled with primary dark and bold white text, marked to repeat across page breaks; zebra striping on body rows with a very light brand tint; thin light borders; fixed DXA widths that sum exactly to the content width; cell padding on every cell; left-aligned cell text.
- **Audience targeting is a design feature.** Early in the document, add a reader-profile → recommended-reading-path table built from the audience-alignment phase. This is the single cheapest way to make a document "speak to" its readers.
- **Callout boxes** for content that must not be skimmed past, with fixed color semantics from the brand's alternative palette: NOTE/info (accent-tinted background), WARNING (yellow/amber tint — irreversible actions, live-impact settings, assumptions), TIP (green tint — recommended practice, decision shortcuts). Implement as a single-cell table with a thick colored left border, a tinted background, and a small bold uppercase label. Scan the text for sentences like "do not…", "be careful…", "assumption:", "practical advice:" — those are callouts trying to escape the paragraph.
- **Code blocks**: monospaced font at ~9pt, light gray background, thin borders with a thick accent bar on the left, and — critically — **left-aligned**. If the document body is justified, code and callout paragraphs must explicitly override to left alignment, or soft line breaks stretch into unreadable gaps.
- **Example inputs / quoted prompts** (things a user would type) as indented italic paragraphs with an accent left border, visually distinct from both body text and code.
- **Bullets and numbered lists** via real numbering definitions, never typed glyphs. Brand the bullet glyph (accent-colored square or dot). Each numbered sequence gets its own numbering instance so lists never continue counting across sections.

## 4. Figures

- **Renumber in reading order.** Source material often has figure numbers in creation order (7, 1, 2, 8…). The delivered document numbers figures 1..N in the order the reader encounters them, and every cross-reference and the figure index are regenerated to match. Automate the numbering — hand-numbering is how the source got broken.
- Captions sit under the image, centered: bold `Figure N.` in primary dark, then the caption text in italic gray, ~9pt. Keep the image paragraph and its caption on the same page (keep-with-next).
- Uniform image width (near content width), centered. Every figure is referenced or at least contextualized by nearby text.
- Generate a **figure index appendix** (number, caption, chapter) from the same data that numbered the figures, so it cannot drift.

## 5. Typography defaults

- One font family throughout; body 10–11pt; line spacing ~1.15–1.2; justified body text is fine for a formal manual, but code, callouts, table cells, and captions are left-aligned.
- Body text in near-black (e.g. `2B3338`), not pure black; metadata and captions in the brand gray.
- Heading scale roughly 19pt / 13.5pt / 11.5pt for H1/H2/H3, all bold, H1–H2 in primary dark, H3 in the neutral gray; headings keep-with-next.
- A4 with 2 cm margins unless the audience is US-based (then Letter with 1"). Compute the content width once and derive every table width from it.

## 6. Build and verify

Producing the file is half the job; the other half is proving it looks right.

1. **Separate content from rendering.** Author the final content as a marked-up intermediate (Markdown or a light custom markup), and generate the DOCX with a script (python-docx or docx-js). This makes figure renumbering, part grouping, and re-styling repeatable instead of manual.
2. **Validate the OOXML schema** after generating (the docx skill ships `validate.py`). The recurring pitfalls are ordering constraints: children of `pPr`, `tcPr`, `tblPr`, border sets (`top → left → bottom → right → insideH → insideV`), and `tcMar` all have a fixed schema order; `tblW` must precede `jc`; python-docx already inserts `tblW`/`tblLayout` on `add_table`/`autofit`, so update the existing element instead of appending a duplicate. Insert at schema position, never blind-append.
3. **Render and look.** Convert to PDF (LibreOffice), rasterize sample pages, and visually inspect at minimum: the cover, the TOC page, one table-heavy page, one figure page, one callout, one code block, and the appendix. This inspection catches what validation cannot: justified code blocks, a metadata table spilling off the cover, a caption orphaned from its image.
4. **When redesigning an existing document, prove nothing was lost.** Split every source paragraph and table cell into sentences, normalize punctuation (smart→straight quotes, dash variants), and probe each sentence against the full text of the new document. Every miss must be explainable as an intentional rewrite (heading renamed, prose converted to a table, cross-reference re-worded) — an unexplained miss is lost content and a blocking failure.
5. Deliver the artifact plus, when useful, the intermediate content file — it is what gets edited next time.

## 7. Self-check before delivery

- Does the palette come from the brand, with a recorded source?
- Cover complete and contained to one page; TOC field present; parts, numbered chapters, header/footer in place?
- Is every enumerable prose block that would scan better as a table, a table?
- Are warnings/tips/assumptions in callouts rather than buried mid-paragraph?
- Code left-aligned, monospaced, shaded?
- Figures numbered in reading order, captioned, indexed in an appendix?
- Schema validation passed, PDF sample pages inspected, content-loss probe clean?

A deliverable that fails any of these is not ready, regardless of how good the prose is.
