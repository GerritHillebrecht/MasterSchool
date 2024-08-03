from ..database import read_from_database, write_to_database
from ...config.config import SUPPORTED_MOVIE_DATA


def add_movie() -> None:
    """
    Loads the required Meta-data for each movie from the config file.
    Prompts the user for each meta-data-item and validates the input. Updates the database accordingly.
    :return:
    """
    movie_data = {prompt["name"]: validated_input(prompt) for prompt in SUPPORTED_MOVIE_DATA}
    write_to_database(read_from_database() + [movie_data])


def validated_input(prompt: dict) -> str:
    """
    Prompts the user for the passed meta-data-item until the validation function accepts the input.
    Also formats the input according to the config file. E.g. the title string cannot have symbols that are used
    within in the .csv of the database. These are replaced.
    :param prompt: The meta-data prompt item from the config file.
    """
    while True:
        user_input = input(f'Enter new {prompt["label"]}: ')
        if prompt["validator"](user_input):
            return prompt["formatter"](user_input) if "formatter" in prompt else user_input
        print(prompt["validator_message"])
