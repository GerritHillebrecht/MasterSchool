import requests

REQUEST_URL = "https://sallysbakingaddiction.com/cookies-n-cream-cookies/"
OUTPUT_FILE_NAME = "OUTPUT.HTML"


def save_to_file(text, file_name):
    with open(file_name, "w") as handle:
        handle.write(text)


def main():
    res = requests.get(REQUEST_URL)
    save_to_file(res.text, OUTPUT_FILE_NAME)


if __name__ == "__main__":
    main()
