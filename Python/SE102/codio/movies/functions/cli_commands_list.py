from .crud import add_movie, list_movies, delete_movie_from_database, update_movie
from .mix import stats, select_random_movie, search_movie, print_movies_by_rating, print_movies_by_release, filter_movies

CLI_COMMANDS_TYPE = list[dict["label": str, "function": callable]]


def get_cli_command_list() -> CLI_COMMANDS_TYPE:
    """
    Returns the whole program-menu as a list of dictionaries, using function pointers (dispatcher-pattern)
    to make the menu work.
    :return:
    """
    return [
        # CRUD functions
        # 1. READ
        {
            "label": "List movies",
            "function": list_movies
        },

        # 2. CREATE
        {
            "label": "Add movie",
            "function": add_movie
        },

        # 3. DELETE
        {
            "label": "Delete movie",
            "function": delete_movie_from_database
        },

        # 4. UPDATE
        {
            "label": "Update movie",
            "function": update_movie
        },

        # 5. Read and mutate
        {
            "label": "Stats",
            "function": stats
        },

        # 6. Random
        {
            "label": "Random movie",
            "function": select_random_movie
        },

        # 7. Search
        {
            "label": "Search movie",
            "function": search_movie
        },

        # 8. Movies sorted by rating
        {
            "label": "Movies sorted by rating",
            "function": print_movies_by_rating
        },

        # 9. Movies sorted by year
        {
            "label": "Movies sorted by year",
            "function": print_movies_by_release
        },

        # 10. Filter movies
        {
            "label": "Filter movies",
            "function": filter_movies
        }
    ]
