from romeo_and_juliet import PLAY as romeo_and_julia_play


def get_words(text):
    """
    This function takes in a text and returns the words of the text as a list.
    :param text: The text to be split into words.
    :type text: str
    :return: Return a list of words.
    :rtype: list of str
    """
    return text.split(" ")


def words_frequency(words):
    """
    Takes in a list of words and returns the occurrence of each words as a dict.
    :param words: The words to be counted
    :type words: list of str
    :return: Return a dictionary with word, count pairs.
    :rtype: dict[str, int]
    """
    frequency_of_words = {}
    for word in words:
        frequency_of_words[word] = frequency_of_words.get(word, 0) + 1
    return frequency_of_words


def top_n_words(freq, n):
    """
    Takes a dictionary and a limiter and returns a sorted dictionary with <n> items.
    :param freq: The dict to be sorted and cut.
    :type freq: dict[str, int]
    :param n: The amount of returned words
    :type n: int
    :return: Returns a sorted dictionary.
    :rtype: dict[str, int]
    """
    return dict(sorted(freq.items(), key=lambda word: word[1], reverse=True)[:n])


def main():
    words = get_words(romeo_and_julia_play)
    frequencies = words_frequency(words)
    for word, count in top_n_words(freq=frequencies, n=50).items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
