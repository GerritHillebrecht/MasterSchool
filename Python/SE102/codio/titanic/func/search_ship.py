MyType = list[dict[str, int | str]]


def print_search_ship(ships: MyType, search_string: str) -> None:
    """
    Prints a list of shipnames based on a search-string.
    """
    matching_ships = [
        ship["SHIPNAME"]
        for ship in ships
        if search_string.lower() in ship["SHIPNAME"].lower()
    ]

    print("Ships matching your search: ")
    for matching_ship in matching_ships:
        print(matching_ship)
