def start_input_loop(number_to_reach):
    """
    This function starts an infinite loop, until the user accumulates a sum of param <number_to_reach>
    :param number_to_reach: The number that the user has to reach to complete the loop.
    :type number_to_reach: int or float
    :return: This function has no return value.
    """
    n = 0  # accumulator

    while n < number_to_reach:
        n += int(input("Enter your number: "))

    print(f"Final sum: {n}")


def main():
    start_input_loop(1000)


if __name__ == "__main__":
    main()
