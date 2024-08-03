# 1 Search and replace
def search_and_replace(file_name: str, search_word: str, replace_word: str):
    try:
        with open(file_name, "r") as file:
            orig_file_data = file.read()
    except Exception:
        raise TypeError("The provided filename could not be found")

    try:
        new_file_name = f"{file_name[:file_name.rfind(".")]}.new.{file_name.split(".").pop()}"
        with open(new_file_name, "w") as file_copy:
            file_copy.write(orig_file_data.replace(search_word, replace_word))
    except Exception:
        raise TypeError("Could not write to the provided filename")

    return file_name


search_and_replace("info.txt", "text", "obnoxious pamphlet")


# 2 - timesheet for months
def create_timesheet_for_month(file_name: str, month: str):
    try:
        with open(file_name, "r") as file:
            orig_file_data = file.read()

    except Exception:
        raise TypeError("Invalid filename.")

    try:
        new_file_name = f"{file_name[:file_name.rfind(".")]}_{month}.{file_name.split(".").pop()}"
        with open(new_file_name, "w") as file_copy:
            file_copy.write(orig_file_data)
    except Exception:
        raise TypeError("Something went wrong.")


def create_timesheet_for_months(file_name: str, months: list[str]):
    for month in months:
        create_timesheet_for_month(file_name, month)


months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
create_timesheet_for_months("timesheet.rtf", months)

# 3 - Country files
countries = [{"name": "Spain",
              "capital_city": "Madrid",
              "currency": "EUR"
              },
             {"name": "United States",
              "capital_city": "Washington",
              "currency": "USD"
              },
             {"name": "Canada",
              "capital_city": "Ottawa",
              "currency": "CAD"
              }
             ]


def create_country_files(countries: list[dict[str, str]]):
    for country in countries:
        with open(f'{country["name"]}.txt', "w") as file_copy:
            file_copy.write(country["capital_city"])


create_country_files(countries)


# 4 - Sounds multiplier
def multiply_sound(file_name: str):
    try:
        with open(file_name, "r") as file:
            original_header = file.readline()
            original_lines = file.readlines()
    except Exception:
        raise TypeError("Consider passing a valid filename")

    for line in original_lines:
        audio_file_name, multiplication_number, audio_output_file = line.strip().split(",")

        try:
            multiplication_number = int(multiplication_number)
        except ValueError:
            print("The number of multiplications should be convertable to int.")

        with open(audio_file_name, "rb") as audio_file:
            audio_data = audio_file.read()

        with open(audio_output_file, "wb") as audio_file_copy:
            for i in range(multiplication_number):
                audio_file_copy.write(audio_data)


multiply_sound("sounds-multiply.csv")
