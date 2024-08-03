from methods.file import create_file
from methods.product import prompt_add_product, list_products, prompt_delete_product, prompt_bought_product
from data.prompts import USER_CHOICE


def menu():
    """
    Show the main menu, get user choice and call the wanted function
    Stops only when user quits
    """
    create_file()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_product()
        elif user_input == 'l':
            list_products()
        elif user_input == 'b':
            prompt_bought_product()
        elif user_input == 'd':
            prompt_delete_product()

        user_input = input(USER_CHOICE)


def main():
    menu()


if __name__ == "__main__":
    main()
