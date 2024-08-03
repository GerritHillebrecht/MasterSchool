from .cli_commands_list import CLI_COMMANDS_TYPE


def start_user_input_loop(commands: CLI_COMMANDS_TYPE) -> None:
    """
    Repeatedly prompts the user for commands until ended by user.
    :param commands: Takes in the list of commands.
    :return: This function does not return a value.
    """
    # Start-up menu.
    print("Menu:\n0. Exit")
    for idx, command in enumerate(commands):
        print(f'{idx + 1}. {command["label"]}')
    print("")

    # Actual input loop.
    while True:
        try:
            user_selected_command = int(input(f"Enter a choice (0-{len(commands)}): "))
        except ValueError:
            print("Please pass your choice as a number.")
            continue

        # len(commands) without (-1) because command 0 (exit) is not listed in the commands list.
        if not 0 <= user_selected_command <= len(commands):
            print("Please choose one of the displayed choices")
            continue

        # Exit if user selects 0.
        if user_selected_command == 0:
            print("Bye!")
            return

        # Execute selected function, (-1) because "0. Exit" is not included in commands-list.
        commands[user_selected_command - 1]["function"]()
