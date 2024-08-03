def print_ships_by_types(ships: list) -> None:
    """
    Prints a numerated list of ship-types with the amount of ships per ship-type.
    """
    ship_types = [ship["TYPE_SUMMARY"] for ship in ships]
    counted_ship_types = {ship_type: ship_types.count(ship_type) for ship_type in set(ship_types)}
    sorted_ship_types = sorted(
        counted_ship_types.items(),
        key=lambda ship_type: ship_type[1],
        reverse=True
    )

    for idx, (ship_name, number_of_ships) in enumerate(sorted_ship_types):
        print(f'{idx + 1}. {ship_name}: {number_of_ships}')
