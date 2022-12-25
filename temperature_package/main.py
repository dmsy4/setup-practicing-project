import argparse
from pathlib import Path

from .draw import plot_fig
from .loader import get_city_mean_annual_temperature, load_dataframe


def main(arguments: argparse.Namespace) -> None:
    csv_path = arguments.csv_path
    start_year = arguments.start_year
    end_year = arguments.end_year
    city = arguments.city
    savefig_path = arguments.savefig_path

    df = load_dataframe(csv_path, start_year, end_year)

    city_avgtemp_series = get_city_mean_annual_temperature(df, city)

    plot_fig(city_avgtemp_series, city, savefig_path)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Программа для вывода графика "
        "среднегодовой температуры в указанном городе "
        "за указанный период"
    )

    parser.add_argument(
        "csv_path",
        type=Path,
        default="./data/GlobalLandTemperaturesByMajorCity.csv",
        help="Путь к csv файлу",
    )
    parser.add_argument(
        "start_year",
        default=-1,
        type=int,
        help="Начальный год для подсчета среднеговой температуры "
        "(-1, чтобы учитывать с наиболее раннего года)",
    )
    parser.add_argument(
        "end_year",
        default=-1,
        type=int,
        help="Конечный год для подсчета среднеговой температуры "
        "(-1, чтобы учитывать до наиболее позднего года)",
    )
    parser.add_argument(
        "--city",
        default="Saint Petersburg",
        type=str,
        help="Название города, для которого будет выведен график "
        "среднегодовой температуры",
    )
    parser.add_argument(
        "--savefig_path",
        default="./figures/",
        type=str,
        help="Путь, по которому будет сохранен график",
    )

    args = parser.parse_args()
    main(args)
