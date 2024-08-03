from math import sqrt


def get_number_from_user() -> int:
    """
    Asks the user to input a number until the received input is valid (a convertable str).
    :return: The converted string (into an int)
    """
    selected_number = ""
    while not is_convertable_to_int(selected_number):
        print("Please enter a valid number.")
        selected_number = input("Enter a number: ")
    return int(selected_number)


def is_convertable_to_int(string: str) -> bool:
    """
    Checks if a given string is digits, so it can be converted into an int.
    :param string: A string that is potentially convertable into an int.
    :return: A boolean whether the input string is convertable into an int.
    """
    return string.isdigit() \
        if not string.startswith("-") \
        else string[1:].isdigit()


def is_valid_number(number: int) -> bool:
    """
    Checks, whether an input number meets all requirements. In this case, that it's an even number.
    :param number: The number to be checked
    :return: A boolean representation whether it's a valid number.
    """
    if number % 2 == 1:
        print("Please enter an even number. We're trying to prove Goldbach's conjecture here.")
        return False
    return True


def list_of_summing_primes(number) -> list[tuple[int, int]]:
    """
    Checks whether an even number is composed of two prime numbers.
    :param number: The even number to be checked.
    :return: A list of tuples representing primes that equal the input number.
    """
    prime_numbers_list = []

    # Only loop half the range (+1) because we're checking numbers from both sides (number - i).
    for i in range(2, int(number / 2) + 1):
        if is_prime_number(i) and is_prime_number(number - i):
            prime_numbers_list.append((i, number - i))
    return prime_numbers_list


def is_prime_number(number_to_be_checked: int) -> bool:
    """
    Checks if a given number is a prime number.
    :param number_to_be_checked: The number to be checked.
    :return: Whether this input number is a prime.
    """
    if number_to_be_checked <= 2:
        return False

    i, is_prime = 2, True
    # shorten the loop by only going up to the square root and exiting when a divisor is found.
    while i < sqrt(number_to_be_checked) and is_prime:
        if number_to_be_checked % i == 0:
            is_prime = False
        i += 1
    return is_prime


def main():
    # Ask user for a valid number until it's a number input
    selected_number = get_number_from_user()

    # if it's an even number, check that number and print the result
    if is_valid_number(selected_number):
        prime_numbers_list = list_of_summing_primes(selected_number)

        if not len(prime_numbers_list):
            print(f"{selected_number} is a miracle and proves Goldbach's conjecture wrong, you're a genius.")
        else:
            for prime_number_1, prime_number_2 in prime_numbers_list:
                print(f"The number {selected_number} equals to the sum of {prime_number_1} and {prime_number_2}")

    # Should check if it's an even number within get_number_from_user, but recursion does just as good of a job
    else:
        main()


if __name__ == "__main__":
    main()
