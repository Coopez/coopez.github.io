# CV source — recovery notes

On 2026-07-23 the `cv/` folder was accidentally deleted during the theme
migration and then partially reconstructed. Status:

## Recovered
- `main.tex`, `text.tex`, `publications.bib` — rebuilt from earlier content,
  with the `\nobibliography{publications}` fix already applied.
- `formal_frontlight_smaller2.jpeg` — extracted from the compiled `cv.pdf`
  (this is the headshot used in the CV and as the website avatar).

## NOT recovered — restore from your own copy
These are needed to compile and were not reconstructable here:
- `res.cls` and `meh.cls` — the resume document classes `main.tex` depends on.
  `res.cls` is a standard class (available on CTAN); `meh.cls` looked like a
  local/modified variant.
- The other portrait photos: `formal_frontlight.jpeg`,
  `formal_frontlight_smaller.jpeg`, `IMG_1806/1807/1814/1828/1830.jpeg`,
  `linkedin.jpeg`.

You almost certainly still have the original CV project (Overleaf or elsewhere)
you copied this from — restoring the two `.cls` files and any photos you want
from there is the quickest fix. The compiled `files/cv.pdf` on the site is
intact and unaffected.
