
def count_capitalize_letters(word: str):
    counter = 0
    for char in word:
        if char.isupper():
            counter += 1
    return counter


def main():
    known_words = set()
    known_emph = set()
    for _ in range(int(input())):
        word = input()
        known_emph.add(word)
        known_words.add(word.lower())
    error_counter = 0
    for check_word in input().strip().split():
        if (check_word.lower() in known_words and check_word not in known_emph) or (
                count_capitalize_letters(check_word) != 1 and not check_word.lower() in known_words):
            error_counter += 1
    print(error_counter)


if __name__ == "__main__":
    main()
