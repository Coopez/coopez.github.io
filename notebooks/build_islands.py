"""Build marimo *islands* HTML (and a card thumbnail) from a notebook.

Run via:  pixi run build-notebooks
Writes:
  _includes/marimo-head.html          -> CDN <script>/<style> (shared, in <head>)
  _includes/notebooks/<name>.html     -> the interactive island body
  images/posts/<name>.png             -> a static preview for the blog card

Both includes are wrapped in {% raw %} so Jekyll never touches the marimo markup.
The __main__ guard is required: marimo's kernel subprocess re-imports this module
on Windows (spawn), and without the guard that re-triggers the build.
"""
import asyncio
from pathlib import Path

from marimo import MarimoIslandGenerator

NOTEBOOK = Path("notebooks/monotonicity.py")
NAME = NOTEBOOK.stem
HEAD_OUT = Path("_includes/marimo-head.html")
BODY_OUT = Path("_includes/notebooks") / f"{NAME}.html"
THUMB_OUT = Path("images/posts") / f"{NAME}.png"


def wrap(html: str) -> str:
    return "{% raw %}\n" + html + "\n{% endraw %}\n"


def make_thumbnail(out: Path, seed: int = 2, roughness: float = 16.0) -> None:
    """A clean, label-free preview of five monotone curves for the blog card."""
    import numpy as np
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    x = np.linspace(0, 1, 300)
    rng = np.random.default_rng(seed)
    kernel = np.ones(25) / 25

    fig, ax = plt.subplots(figsize=(7, 4.0))
    for _ in range(5):
        noise = np.convolve(rng.standard_normal(x.size), kernel, mode="same")
        f = np.cumsum(np.log1p(np.exp(noise * roughness)))
        f = (f - f[0]) / (f[-1] - f[0])
        ax.plot(x, f, lw=2.6, alpha=0.9)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=110, bbox_inches="tight", transparent=True)
    plt.close(fig)


async def main() -> None:
    gen = MarimoIslandGenerator.from_file(str(NOTEBOOK), display_code=False)
    await gen.build()
    HEAD_OUT.write_text(wrap(gen.render_head()), encoding="utf-8")
    BODY_OUT.parent.mkdir(parents=True, exist_ok=True)
    # include_init_island=False: drops the non-reactive "Initializing..." spinner
    # island, which the islands runtime never clears once mounted.
    BODY_OUT.write_text(wrap(gen.render_body(include_init_island=False)), encoding="utf-8")
    make_thumbnail(THUMB_OUT)
    print(f"wrote {HEAD_OUT}, {BODY_OUT}, {THUMB_OUT}")


if __name__ == "__main__":
    asyncio.run(main())
