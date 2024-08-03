# All non-default library imports have import-errors for pylint.
# Program works, but lint can't find them. Maybe tell me in the code-comments
# how to fix that? My mentor is currently ill and I can't ask him.

from data.load_data import load_data

from func.top_countries import print_top_countries
from func.show_countries import print_show_countries
from func.search_ship import print_search_ship
from func.ships_by_type import print_ships_by_types
from map.func_draw_map import draw_map
from histogram.func_speed_histogram import save_file_speed_histogram

JSON_DATA_FILE_PATH = "data/ships_data.json"


def get_cli_command_dict() -> dict[str, dict[str, callable]]:
    """
    Returns a dictionary with all available cli-prompts.
    """
    return {
        "show_countries": {
            "label": "show_countries",
            "function": lambda ships, _: print_show_countries(ships)
        },
        "top_countries": {
            "label": "top_countries <num_countries>",
            "function": lambda ships, number_of_countries: print_top_countries(
                ships,
                number_of_countries[0]
            )
        },
        "ships_by_types": {
            "label": "ships_by_types",
            "function": lambda ships, _: print_ships_by_types(ships)
        },
        "search_ship": {
            "label": "search_ship <part_of_shipname>",
            "function": lambda ships, search_string: print_search_ship(ships, search_string[0])
        },
        "speed_histogram": {
            "label": "speed_histogram",
            "function": lambda ships, _: save_file_speed_histogram(ships)
        },
        "draw_map": {
            "label": "draw_map",
            "function": lambda ships, _: draw_map(ships)
        }
    }


def start_command_input_loop(ship_data: list) -> None:
    """
    Starts an infinite loop of command prompts until cancelled by user.
    Executes valid commands from command_dictionary
    """
    commands = get_cli_command_dict()

    while True:
        user_input = input().strip()

        if user_input == "help":
            for command in commands.values():
                print(command["label"])
            continue

        if user_input.count(" ") > 1:
            print('Invalid input format. Enter "help" to see valid input formats.')
            continue

        command, *value = user_input.split()

        if command in commands:
            commands[command]["function"](ship_data, value)
            continue

        print(f"Unknown command {command}")


def mini_tasks(ships: list) -> None:
    """
    Mini tasks. Not part of the actual program.
    """
    # 1 Print how many ships there are in the file.
    print(f"There are {len(ships)} ships in the file.")

    for ship in ships:
        # 2 Print all the names of all the ships.
        print(ship["SHIPNAME"])

        # 3 Print all the countries of the ships.
        print(f'from {ship["COUNTRY"]}', end="\n\n")

    # 4 Print all the countries of the ships without duplicates
    unique_country_list = sorted(set(ship["COUNTRY"] for ship in ships))
    for idx, country in enumerate(unique_country_list):
        print(f"{idx + 1}. {country}")
    print(f"The ships originate from {len(unique_country_list)} different countries.")


def main():
    """
    Fetches the main data from a json-file. Starts the input loop.
    """
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    json_imported_data = load_data(JSON_DATA_FILE_PATH)
    # mini_tasks(json_imported_data["data"])
    start_command_input_loop(json_imported_data["data"])


if __name__ == "__main__":
    main()
