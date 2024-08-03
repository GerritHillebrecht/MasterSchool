# SETTINGS
NAME_BOT = "__BOT__"
COMBINED_STEP_SIZE = 4
MIN_STICKS = 1
MAX_STICKS = 3


def prompt_player_name() -> str:
    """
    Prompts the player to input the player's name.
    :return: The name of the player
    """
    return input("Select your name: ")


def prompt_number_of_total_sticks() -> int:
    """
    Prompts the player to input the number of sticks to play.
    Denies multiple of four, so bot can win.
    :return: The selected number by the player.
    """
    while True:
        try:
            number_of_sticks = int(
                input("How many sticks do you want to play (default is 21)? ")
            )
        except ValueError:
            print("Please provide your selection as an integer.")
            continue

        if not number_of_sticks % COMBINED_STEP_SIZE == 0:
            print("_____ GAME IS STARTING ____", end="\n\n")
            return number_of_sticks

        print("This number is not selectable, please choose differently ;-)")


def get_selection_bot(number_of_sticks: int) -> int:
    """
    The bot always takes as many sticks as needed to reach a multiple of 4.
    :param number_of_sticks: The amount of sticks left.
    :return: The number of sticks the bot takes.
    """
    return number_of_sticks % COMBINED_STEP_SIZE


def prompt_players_amount_of_sticks() -> int:
    """
    Prompts the player to choose the amount of sticks to take.
    Checks that the chosen amount is within the 1-3 range.
    :return: The chosen amount of the player.
    """
    while True:
        try:
            amount_of_sticks_chosen = int(
                input("Select the amount of sticks you want to take: ")
            )
        except ValueError:
            print("Please insert your selection as an integer.")
            continue

        if MIN_STICKS <= amount_of_sticks_chosen <= MAX_STICKS:
            return amount_of_sticks_chosen

        print(f"Please choose a number between {MIN_STICKS} and {MAX_STICKS}.")


def print_rest_sticks(remaining_sticks: int) -> None:
    """
    Prints how many sticks are left.
    :param remaining_sticks: The amount of remaining sticks.
    :return: This function has no return value.
    """
    print(f"There are {remaining_sticks} sticks left.", end="\n\n")


def print_players_turn(
        sticks_taken: int,
        player: str
) -> None:
    """
    Prints the turn of the selected player.
    :param sticks_taken: The number of sticks taken by the selected player.
    :param player: The name of the player.
    :return: This function has no return value.
    """
    print(f"{player} takes {sticks_taken} sticks.")


def execute_turn(
        sticks_total: int,
        sticks_taken: int,
        player: str
) -> int:
    """
    Executes the turn. Prints updated remaining sticks and the players turn.
    :param sticks_total: The remaining sticks before the turn.
    :param sticks_taken: The sticks taken in this turn.
    :param player: The player taking the sticks.
    :return: The remaining sticks after the turn.
    """
    print_players_turn(sticks_taken, player)
    print_rest_sticks(sticks_total - sticks_taken)
    return sticks_total - sticks_taken


def prompt_restart_game() -> bool:
    """
    Prompts the user whether he wants to play again.
    :return: Boolean value if he wants to try again.
    """
    while True:
        user_prompt = input("Want to try again (Y/N)? ")
        if user_prompt.lower() in ["y", "n"]:
            return user_prompt.lower() == "y"
        print('Please select "Y" or "N"')


def start_game() -> bool:
    """
    Starts the game and returns whether the player wants a rematch.
    Prompts for the player name and the amount of sticks to play for.
    Loops through the turns until the bot won.
    :return: A boolean whether the player wants a rematch.
    """
    print("""
    Welcome to the sticks game.
    Your goal is to take the last of the sticks.
    You're playing against a bot who starts the game.
    Good luck.
    """)
    player_name = prompt_player_name()
    sticks_total = prompt_number_of_total_sticks()

    while True:
        # Turn bot
        sticks_total = execute_turn(
            sticks_total,
            get_selection_bot(sticks_total),
            NAME_BOT
        )

        # Check winner
        if sticks_total <= 0:
            print(f"Better luck next time, {NAME_BOT} won!")
            return prompt_restart_game()

        # Player turn
        sticks_total = execute_turn(
            sticks_total,
            prompt_players_amount_of_sticks(),
            player_name
        )


def main() -> None:
    """
    Loops the start_game function until the player gives up.
    """
    while True:
        if not start_game():
            print("Bye!")
            break


if __name__ == "__main__":
    main()
