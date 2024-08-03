# The return type is always converted to float. This is not done by mistake.
# If this is considered not following the instructions, please ignore the float conversion in the calculate function.
# Returning lists may not be very elegant, but it was chosen for reusability of the calculate function.

# Remark: Usually code should use as little comments as possible and be self-explanatory by using good variable names.
# Since this is the first coding challenge for me and the tutors strongly recommended using as many comments as
# possible, I might have overdone it a little. Please let me know if this is considered good practice for challenges.

from math import inf
from math import ceil


def calculate(operand_1, operand_2, operator):
    """
    The function takes two operands [int] and the operator for the equation [+,-,*,/,~] as inputs.
    It returns the result of the equation. All results are returned as float-values to guarantee uniform returns.
    :param operand_1: The first operand.
    :type operand_1: int
    :param operand_2: The second operand.
    :type operand_2: int
    :param operator: The operator as string [+,-,*,/,~]
    :type operator: str
    :returns: The result as a list. Access it by res[0]. Remainder operations return a Tuple ([0] whole number, [1] remainder).
    :rtype: list of float
    """

    # depending on the operator, return the result accordingly
    if operator == "+":
        return [float(operand_1 + operand_2)]

    if operator == "-":
        return [float(operand_1 - operand_2)]

    if operator == "/":
        # Prevent division by 0.
        if operand_2 == 0:
            print("Dividing by zero is not supported by this calculator.")
            return [inf]
        return [float(operand_1 / operand_2)]

    if operator == "*":
        return [float(operand_1 * operand_2)]

    if operator == "~":
        remainder = operand_1 % operand_2

        # Flooring returns wrong values if the result is negative
        if ((operand_1 < 0 or operand_2 < 0) and not (operand_1 < 0 and operand_2 < 0)) and remainder != 0:
            # Ceil to the closer whole number when negative
            return [float(ceil(operand_1 / operand_2)), float(remainder)]
        else:
            return [float(operand_1 // operand_2), float(remainder)]


def start_calculator(calculations):
    """
    For the number of calculations specified in param calculations user-inputs for equations will be prompted.
    The result of each equation will be printed. The calculator supports [+,-,*,/,~].
    :param calculations: The number of calculation needed to be done
    :type calculations: int
    :return: The function does not return a value.
    :rtype: None
    """
    for i in range(calculations):
        # Prompt the user for each equation.
        user_input = input("What do you want to calculate? ")

        # Define all supported operators
        supported_operators = ["+", "-", "*", "/", "~"]

        # Find the operator-index
        operator_index = find_operator_index(user_input, supported_operators)

        # Split the user input-string at the operator index
        operator = user_input[operator_index]
        operand_1 = int(user_input[:operator_index])
        operand_2 = int(user_input[operator_index + 1:])

        # Pass the operands and operator and save the result in a variable
        result = calculate(operand_1, operand_2, operator)

        # Print the results
        print(f"The answer is {result[0]}")

        # The remainder calculation requires two lines of output
        if len(result) > 1:
            print(f"The remainder is {result[1]}")


def find_operator_index(user_input, operators):
    """
    Use this function to find the index of an operator in an equation (str). Negative numbers are supported.
    :param user_input: User provided equation as str.
    :type user_input: str
    :param operators: All Supported operators
    :type operators: list of str
    :return: The Index of the operator of the equation as int.
    :rtype: int
    """

    # loop the user-input to find the indices of all operators (possibly multiple).
    # We need to save all of them to support negative numbers.
    operator_indices = []
    for j in range(len(user_input)):
        if user_input[j] in operators:
            operator_indices.append(j)

    # If the user chooses unsupported operator
    if len(operator_indices) == 0:
        print("Chosen operation is not supported. Supported types are +, -, *, / and ~")
        return None

    # Of all found operators choose the right one
    # If all operands are positive
    if len(operator_indices) == 1:
        return operator_indices[0]
    # If both operands are negative
    elif len(operator_indices) == 3:
        return operator_indices[1]
    # If one of them is negative
    else:
        if user_input[operator_indices[0]] == "-":
            return operator_indices[1]
        else:
            return operator_indices[0]


# Greet the user to indicate that the calculator is running.
print("Welcome to the Python calculator!")

# Prompt the user for the amount of calculations to be done.
number_of_calculations = int(input("How many calculations do you want to do?"))

# Pass the number of calculations to the init-function
start_calculator(number_of_calculations)
