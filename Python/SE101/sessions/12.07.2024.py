# 1
def is_even():
    return int(input("Give me a number")) % 2 == 0


# 2
def type_of_number():
    num = int(input("Give me a number"))

    if num < 0:
        return f"{num} is negative"
    elif num > 0:
        return f"{num} is positive"
    else:
        return "You entered zero"


# 3
def compute_winner(your_choice, opponent_choice):
    """ Play Rock Paper Scissors """
    selectable_choices = ["rock", "paper", "scissors"]

    # check if choices are made properly
    if your_choice.lower() not in selectable_choices or opponent_choice.lower() not in selectable_choices:
        return "☝️ Please select Rock, Paper or Scissors"

    # Define winners - [0] beats [1] - as tuples
    winning_conditions = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]

    # Guard clause for draws
    if your_choice == opponent_choice:
        return "✨ You played a draw"

    # Check winner
    for winning_condition in winning_conditions:
        if your_choice.lower() == winning_condition[0]:
            if opponent_choice.lower() == winning_condition[1]:
                return f"Your selection of {your_choice} beats {opponent_choice}: You win 🥳"
            else:
                return f"Your selection of {your_choice} loses to {opponent_choice}: You lose 😔"


def play_game():
    print(compute_winner(input("You select (Rock, Paper or Scissors): "),
                         input("Your opponent selects (Rock, Paper or Scissors):")))


play_game()
