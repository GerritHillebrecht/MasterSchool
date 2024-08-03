from string import ascii_lowercase, ascii_uppercase

BOOK_FILE_NAME = "encrypted_book.txt"


def get_book_content(file_path: str) -> str:
    """
    Reads content of file
    :param file_path: path to file
    :return: content of file
    """
    with open(file_path, "r", encoding="utf8") as handle:
        return handle.read()


def char_frequency_map(text: str) -> list:
    """
    Takes a text and returns the frequency of
    every character in the text.
    :param text: text to be analysed
    :return: A list of tuples for each char with its count.
    """
    return sorted(
        {
            char: text.count(char)
            for char in set(text)
            if char in ascii_lowercase + ascii_uppercase
        }.items(),
        key=lambda char: (-char[1], char[0])
    )


def get_words_by_length(text, word_length: int) -> list:
    """
    Takes a text and returns for a given word-length all
    words with that length.
    :param text: The text to be split into words.
    :param word_length: The length of the word.
    :return: A list of words with the given length.
    """
    return [word.strip() for word in text.split() if len(word) == word_length]


def get_sorted_frequency_of_word(words: list):
    """
    Sorts words by its occurrence.
    :param words: list of words to be counted.
    :return: A sorted list of tuples consisting of the word and it's count.
    """
    return sorted(
        {
            word: words.count(word)
            for word in set(words)
        }.items(),
        key=lambda word: (-word[1], word[0])
    )


def main():
    """
    Was used to do a frequency check for each letter. Since that
    didnt lead anywhere, the most common 2, 3 and 4-letter words
    where compared to the most frequent words. 14 letters were
    recognized. By printing undecrypted letters in lower-case,
    the rest could be guessed.
    :return:
    """
    encrypted_book = get_book_content(BOOK_FILE_NAME)
    mapping = {}

    words_by_frequency = [
        [
            ["O", "F"],
            ["T", "O"],
        ],
        [
            ["T", "H", "E"],
            ["A", "N", "D"],
            ["W", "A", "S"],
        ],
        [
            ["T", "H", "A", "T"],
            ["W", "I", "T", "H"],
            ["F", "R", "O", "M"],
            ["H", "A", "V", "E"],
            ["T", "H", "I", "S"],
            ["W", "E", "R", "E"],
        ]
    ]

    for word_category in words_by_frequency:
        words_sorted_by_count = get_sorted_frequency_of_word(
            get_words_by_length(encrypted_book, len(word_category[0]))
        )
        for idx, word in enumerate(word_category):
            for char_idx, char in enumerate(word):
                mapping[words_sorted_by_count[idx][0][char_idx].upper()] = char

    print(f"{len(mapping)} letters translated.")
    print(f"lower-case letters are not in the dict yet.")

    decrypted = ""

    for i in range(500):
        if encrypted_book[i].upper() in mapping:
            decrypted += mapping[encrypted_book[i].upper()]
        else:
            decrypted += encrypted_book[i]

    # print(decrypted)

    # Manually decrypting the rest
    mapping["E"] = "K"
    mapping["Q"] = "P"
    mapping["O"] = "U"
    mapping["J"] = "Y"
    mapping["N"] = "L"
    mapping["H"] = "C"
    mapping["Z"] = "G"
    mapping["B"] = "B"

    decrypted = ""

    # Retesting for missing characters
    for i in range(500, 2000):
        if encrypted_book[i].upper() in mapping:
            decrypted += mapping[encrypted_book[i].upper()]
        else:
            decrypted += encrypted_book[i]
    # print(decrypted)

    mapping["S"] = "D"
    mapping["Y"] = "Z"
    mapping["G"] = "X"

    for i in range(500, 2000):
        if encrypted_book[i].upper() in mapping:
            decrypted += mapping[encrypted_book[i].upper()]
        else:
            decrypted += encrypted_book[i]

    print(decrypted)
    # mapping = {
    #     "A": "S",
    #     "B": "B",
    #     "C": "D",
    #     "D": "F",
    #     "E": "K",
    #     "F": "H",
    #     "G": "J",
    #     "H": "C",
    #     "I": "E",
    #     "J": "Y",
    #     "K": "T",
    #     "L": "V",
    #     "M": "W",
    #     "N": "L",
    #     "O": "U",
    #     "P": "X",
    #     "Q": "P",
    #     "R": "R",
    #     "S": "Q",
    #     "T": "I",
    #     "U": "O",
    #     "V": "M",
    #     "W": "N",
    #     "X": "A",
    #     "Y": "Z",
    #     "Z": "G"
    # }


if __name__ == "__main__":
    print(len("""LL REDOICE TO HEAR THAT NO DISASTER HAS ACCOMPANIED THE
COMMENCEMENT OF AN ENTERPRISE WHICH YOU HAVE REGARDED WITH SUCH EVIL
FOREBODINGS. I ARRIVED HERE YESTERDAY, AND MY FIRST TASK IS TO ASSURE
MY DEAR SISTER OF MY WELFARE AND INCREASING CONFIDENCE IN THE SUCCESS
OF MY UNDERTAKING."""))
    main()
