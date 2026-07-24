import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    # Transparent figures so the page background (light or dark) shows through.
    plt.rcParams.update({
        "savefig.transparent": True,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
    })

    roughness = mo.ui.slider(steps=[0, 8, 16, 32], value=16, label="roughness", show_value=True)
    seed = mo.ui.slider(1, 5, value=1, label="seed", show_value=True)
    mo.hstack([roughness, seed], justify="start", gap=2)
    return mo, np, plt, roughness, seed


@app.cell
def _(np, plt, roughness, seed):
    n_functions = 5
    x = np.linspace(0, 1, 300)
    rng = np.random.default_rng(int(seed.value))

    window = 25
    kernel = np.ones(window) / window  # smooth the increments -> smooth curves

    ink = "#888888"  # mid-grey: legible on both light and dark backgrounds
    fig, ax = plt.subplots(figsize=(7, 4.5))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    for _i in range(n_functions):
        noise = np.convolve(rng.standard_normal(x.size), kernel, mode="same")
        increments = np.log1p(np.exp(noise * roughness.value))  # softplus: positive
        f = np.cumsum(increments)
        f = (f - f[0]) / (f[-1] - f[0])  # normalise to [0, 1]
        ax.plot(x, f, lw=2.2, alpha=0.9)

    ax.set_xlabel("x", color=ink)
    ax.set_ylabel("f(x)", color=ink)
    ax.set_title("Five monotonic increasing functions", color=ink)
    ax.tick_params(colors=ink)
    ax.grid(True, alpha=0.25, color=ink)
    for side, spine in ax.spines.items():
        spine.set_visible(side in ("left", "bottom"))
        spine.set_color(ink)
    fig
    return


if __name__ == "__main__":
    app.run()
