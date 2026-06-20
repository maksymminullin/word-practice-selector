import csv
from pathlib import Path


def get_all_csv_files(base_directory: str | Path) -> list[Path]:

    folder = Path(base_directory)

    files = list(folder.rglob("*.csv"))

    return files


def main():
    print("")


if __name__ == "__main__":
    main()
