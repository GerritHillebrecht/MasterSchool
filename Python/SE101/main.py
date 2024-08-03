# This is a sample Python script.
# Press Strg+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from statistics import mean


def square_number(number_to_square: int) -> int:
    return number_to_square ** 2


def square_list(list_to_square: list[int]) -> list[int]:
    return [square_number(number_to_square) for number_to_square in list_to_square]


def get_user_selection(numbers, func_dict):
    while True:
        selected_operand = input("""
    What would you like to do with your grades?
    NUM = Print the num of grades.
    AVG = Print the average grade.
    MAX = Print the maximum grade.
    MIN = Print the minimum grade.
    """)
        if selected_operand in dict:
            break

    return func_dict[selected_operand](numbers)


def square(number):
    return number ** 2


def main():
    func_dict = {
        "NUM": len,
        "AVG": mean,
        "MAX": max,
        "MIN": min
    }

    # print(get_user_selection([10], func_dict))
    asd = map(square, [2, 3, 4, 5, 6, 7])
    print(asd)
    print(type(asd))


if __name__ == "__main__":
    main()
