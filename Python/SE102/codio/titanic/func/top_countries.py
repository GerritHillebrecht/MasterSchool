def print_top_countries(ships: list, number_of_countries: str) -> None:
    """
    Prints a numerated list of the countries with the most ships.
    Takes the number of countries to be printed as an argument.
    """
    try:
        number_of_countries = int(number_of_countries)
    except ValueError:
        print("Please pass a numerical value as the <num_countries>")
        return

    country_list = [ship["COUNTRY"] for ship in ships]
    counted_countries = {country: country_list.count(country) for country in set(country_list)}
    sorted_countries = sorted(
        counted_countries.items(),
        key=lambda country: country[1],
        reverse=True
    )

    for idx, (country, count) in enumerate(sorted_countries[:number_of_countries]):
        print(f'{idx + 1}. {country}: {count}')
