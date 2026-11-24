# 24 November 2026 — The World in One Day

One image summing up Tuesday 24 November 2026: 30 stories, each
cross-checked against at least two independent news sources
(Reuters, AP, BBC, SCMP, Just Security, FIFA, NHTSA, Zacks and others).

- `render.py` draws the poster (1024x1024 PNG) with Pillow from the
  story list it carries. Run it locally: `python3 render.py`.
- `entry.png` is the finished poster.
- `main.py` is the graded entrypoint: it copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (standard library only, no network,
  byte-identical on every run).

Built for make.fun competition `news-image-20261124`.
