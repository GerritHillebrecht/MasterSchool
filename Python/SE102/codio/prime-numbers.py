def get_range():
    """
    Lets the user give a range of positive integers and returns them as a tuple.
    :return: Tuple of integers
    :rtype: (int, int)
    """
    return int(input("Start of range: ")), int(input("End of range: "))


def is_divisible_by(number, by):
    """
    Takes in a number and a divisor. Returns if it is divisible without a remainder.
    :param number: int
    :type number: The number that is checked
    :param by: int
    :type by: The divisor
    :return: Returns whether <number> is divisible by <by> as a boolean
    """
    return number % by == 0


def is_prime_number(number):
    """
    Checks whether the passed number is a boolean.
    :param number: The number to be checked.
    :type number: int
    :return: Returns whether <number> is a prime as a boolean.
    :rtype: bool
    """
    if number <= 1:
        return False

    for i in range(2, number):
        if is_divisible_by(number, i):
            return False
    return True


def primes_in_range(start_of_range, end_of_range):
    """
    Calculates all prime numbers within a given range.
    :param start_of_range: The start of the range.
    :type start_of_range: int
    :param end_of_range: The end of the range.
    :type end_of_range: int
    :return: The prime numbers within a given range as a list.
    :rtype: list of int
    """
    prime_numbers = []
    for i in range(start_of_range, end_of_range):
        if is_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers


def main():
    # Get the range from the user
    start_range, end_range = get_range()

    # get the list of all prime number inside the range
    prime_numbers = primes_in_range(start_range, end_range)

    # print the list
    for prime_number in prime_numbers:
        print(f"The number {prime_number} is prime")


if __name__ == "__main__":
    main()
