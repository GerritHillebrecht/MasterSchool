# I wrote the code before going through the steps in codio,
# so if some function-names or the structure are off, i'm sorry.


from .config import WELCOME_MESSAGE
from .functions import get_cli_command_list, start_user_input_loop


def main() -> None:
    """
    Welcomes the user and starts the command prompt-loop.
    :return: Does not return a value.
    """
    # inform the user that the program is running by sending a welcome-message.
    print(WELCOME_MESSAGE)

    # Get and pass all available user-commands to the loop-starting-function.
    start_user_input_loop(get_cli_command_list())


if __name__ == "__main__":
    main()
