def main():
    while True:
        file_name = input("What is your name? ")
        if len(file_name) > 2:
            break

    with open(f"{file_name}.txt", "w") as f:
        f.write(f"Hello, {file_name}!")


if __name__ == "__main__":
    main()
