from ...config import SELECTED_DATABASE
from .storage_csv_methods import write_database_csv, read_database_csv
from .storage_json_methods import write_database_json, read_database_json


def write_to_database(movies: list[dict]) -> None:
    if SELECTED_DATABASE == "JSON":
        write_database_json(movies)
    else:
        write_database_csv(movies)


def read_from_database() -> list[dict]:
    return read_database_json() if SELECTED_DATABASE == "JSON" else read_database_csv()
