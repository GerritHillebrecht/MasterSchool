from statistics import mean

SUBJECTS_OF_STUDENTS = ["English", "Math"]


def get_number_of_students_to_grade() -> int:
    """
    Prompts the user how many students should be graded.
    Loops until positive integer is returned.
    :return: Number of students to be inserted.
    """
    while True:
        prompt = "Enter the number of students: "
        exception_message = "Please enter the number of students as integer"
        number_of_students = int(prompt_integer_input(prompt, exception_message))

        if number_of_students > 0:
            return number_of_students
        else:
            print("Expected a positive integer")


def get_grade(subject: str) -> float:
    """
    Prompts the user to input a grade between 1-100. Prompts until a valid input is given.
    :param subject: The subject that the grade is asked for. E.g. English, Sport, Math.
    :return: Returns the grade as a float.
    """
    prompt = f"Enter {subject} grade: "
    # Two while loops:
    while True:  # Outer loop checks if input is between 0 and 100
        grade = prompt_integer_input(prompt, "Grades should be entered as integers.")

        if is_valid_grade(grade):
            return grade
        else:
            print("Please enter a grade between 0 and 100.")


def prompt_integer_input(prompt: str, exception: str) -> float:
    """
    Prompts the user for an integer value and only returns when the input is valid.
    :param prompt: The Prompt displayed to the user.
    :param exception: The displayed output for invalid input
    :return: A valid numerical input as float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(exception)


def is_valid_grade(grade: float) -> bool:
    """
    Checks the validity of the grade. In this case, if it's gt 0.
    :param grade: The grade to check as float
    :return: Whether the grade is greater than 0.
    """
    return 0 <= grade <= 100


def get_student_info(subjects: list[str]) -> dict[str, str | float]:
    """
    Prompts user input for student data, asking for name and grades.
    :param subjects: The subjects to prompt for
    :return: A Dictionary of student-data.
    """

    # Dictionary keys should be lowercase, but the codio-assignment required capitalized keys.
    student_info = {
        "Name": input("Enter student name: "),  # No str validation required, "88" is a valid student name.
    }

    for subject in subjects:
        student_info[subject] = get_grade(subject)

    return student_info


def calculate_average_grades(students: list[dict[str, str | float]]) -> tuple[dict[str, float], float]:
    """
    Calculates the average grade per subject and the total average.
    :param students: List of Students including their name and grades as a dict.
    :return: A Tuple of the average grade per student as well as the overall grade.
    """
    subjects: dict[str, float] = {}

    # This code appeared a little too hard to read.
    # subjects = [subjects.get(subject, 0) + grade / len(students) for student in students for subject, grade in
    #        student.items() if subject != "Name"]

    for student in students:
        for subject, grade in student.items():
            if subject == "Name":
                continue
            subjects[subject] = subjects.get(subject, 0) + grade / len(students)

    overall_average = mean([grade for subject, grade in subjects.items()])
    return subjects, overall_average


def print_student_info(students: list[dict[str, str | float]]) -> None:
    """
    Takes in a list of dictionaries representing student-data. Prints the student-info and
    values based on the dictionary-data such as average and best grade.
    :param students: list of dictionaries representing student-data.
    :return: This function has no return value.
    """
    print("Student Information:")
    for student in students:
        grades = [grade for subject, grade in student.items() if subject != "Name"]
        avg = mean(grades)
        best = max(grades)
        print(f'Student: {student["Name"]}, Best Grade: {best}, Average Grade: {avg}')


def print_overall_info(student_info_list: list[dict[str, str | float]]) -> None:
    average_grades_per_subject, overall_average_grade = calculate_average_grades(student_info_list)
    print("\nAverage grades per subject:")
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")


def main():
    """
    The program fetches data from the user, saves it as a dictionary
    and prints computed values based on the input. The main function
    prompts the user for the amount of student-data required to input.
    Afterward prompts the user for the specified amount of data and prints it.
    Finally, the average grades for each subject and the overall average are printed.
    :return:
    """
    # Prompt for user-data
    number_of_students = get_number_of_students_to_grade()
    students_info_list = [get_student_info(SUBJECTS_OF_STUDENTS) for i in range(number_of_students)]

    # Print results
    print_student_info(students_info_list)
    print_overall_info(students_info_list)


if __name__ == "__main__":
    main()
