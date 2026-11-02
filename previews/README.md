# Homepage review wireframe

Open `homepage.html` in a browser. It is a self-contained, local HTML preview with no external fonts, dependencies or network requests.

The copy source is `../docs/content/P001-home.md`. After changing that file or `homepage.css`, regenerate with:

```sh
python3 previews/build_preview.py
```

This is a draft copy and layout review artifact, not the production Astro implementation. Navigation moves between homepage sections. Links intended for future pages disclose their planned destination; no form submissions are collected. The text mark and installed fonts are wireframe stand-ins.

Review the proposition, amount of copy, prominence of the six domains and the invitation to participate. Exact fonts and palette values remain subject to review.

Browser rendering and interaction verification are pending. Static checks are recorded in `../docs/qa/homepage-wireframe.md`.
