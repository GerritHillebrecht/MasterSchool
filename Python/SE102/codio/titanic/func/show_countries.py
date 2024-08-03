def print_show_countries(ships: list) -> None:
    """
    Prints a list of all countries sorted alphabetically.
    """
    country_list = sorted(set(ship["COUNTRY"] for ship in ships))

    for country in country_list:
        print(country)
