from os import makedirs
from os.path import join
from pathlib import Path

from matplotlib.pyplot import close, figure, savefig, subplot
from pandas import Series


def plot_fig(series: Series, city: str, savefig_path: Path) -> None:
    fig_filename = f"annual_temperature_in_{city}.png".replace(" ", "-")
    makedirs(savefig_path, exist_ok=True)

    figure(figsize=(8, 5), dpi=300)
    ax = subplot()

    temp = series.values
    dates = series.index

    ax.set_title(f"График среднегодовой температуры в городе {city}")
    ax.plot(dates, temp)
    ax.set_xlabel("Год")
    ax.set_ylabel("Температура, °C")
    ax.grid()

    savefig(join(savefig_path, fig_filename), bbox_inches="tight")
    close()
    return
