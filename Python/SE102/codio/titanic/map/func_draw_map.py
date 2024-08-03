import webbrowser
import folium

MAP_STARTING_POS = (53.53113, 9.916946)
MAP_INITIAL_ZOOM = 3


def draw_map(ships: list) -> None:
    """
    Creates a map.html and tries to open it in the browser.
    :param ships: List of all ships to be drawn on the map.
    """
    map_object = folium.Map(location=MAP_STARTING_POS, zoom_start=MAP_INITIAL_ZOOM)

    for ship in ships:
        folium.Marker(
            location=[ship["LAT"], ship["LON"]],
            popup=f'<span style="white-space: nowrap; display: block;">'
                  f'{ship["SHIPNAME"]}'
                  f'</span>'
                  f'<span style="white-space: nowrap; display: block;">'
                  f'Current location: {ship["CURRENT_PORT"]}'
                  f'</span>'
                  f'<span style="white-space: nowrap; display: block;">'
                  f'Origin: {ship["COUNTRY"]} - Type: {ship["TYPE_SUMMARY"]}'
                  f'</span>'
        ).add_to(map_object)

    map_object.save("map.html")
    webbrowser.open("map.html")

    print(
        "The map should be displayed in a new window.\n"
        "If the webbrowser library is not supported, kindly find it in map.html"
    )
