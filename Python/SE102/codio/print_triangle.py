def print_triangle(n: int) -> None:
    """
    Splits the given integer in two loops, for the upper and lower part of the triangle.
    :param n: Number of loop repetitions.
    :return: None
    """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print()
    for i in range(1, n):
        for j in range(1, n - i + 1):
            print(f"{j} ", end="")
        print()


def print_multiplication_table(n: int) -> None:
    """
    Loops through "n" twice and for rows and cols and prints the data-table.
    :param n: Number of loop repetitions.
    """
    end = "\t"
    for row in range(0, n + 1):
        for col in range(0, n + 1):
            if col == 0 and row == 0:
                print(" ", end=end)
                continue
            if row == 0:
                print(col, end=end)
                continue
            if col == 0:
                print(row, end=end)
                continue

            print(col * row, end=end)
        print("")


def prompt_function_input() -> int:
    """
    Returns a user input for the functions as int.
    :return: The validated number as int.
    """
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            print("Please insert an integer.")
            continue


def prompt_function_type() -> str:
    """
    Returns the selected function type, validated.
    :return:
    """
    while True:
        function_type = input(f'Please enter command ({"/".join(dispatcher.keys())}): ')
        if function_type in dispatcher:
            return function_type
        print("You do know how to read, dont you?")


def start_program():
    """
    Prompts the user for the function-input and the function-type, dispatches
    the selected function.
    """
    while True:
        function_input = prompt_function_input()

        # Exit the program if the user indicates it.
        if function_input == -1:
            print("Bye!")
            return

        function_type = prompt_function_type()
        dispatcher[function_type](function_input)


dispatcher = {
    "triangle": print_triangle,
    "mp": print_multiplication_table
}


def main() -> None:
    """
    Starts the program. "start_program" could be inside here instead, but this feels even cleaner.
    """
    start_program()


if __name__ == "__main__":
    main()
