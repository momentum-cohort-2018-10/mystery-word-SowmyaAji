
import random
easy_words = []
medium_words = []
hard_words = []
with open("words.txt") as new_file:
    for word in new_file.readlines():
        word = word.strip()
        if len(word) <= 6:
            easy_words.append(word)

        if len(word) > 6 and len(word) <= 8:
            medium_words.append(word)

        if len(word) > 8:
            hard_words.append(word)


def choose_difficulty():
    level = input("Choose E, M or H for easy, medium or hard words").upper()

    if level == "E":
        secret_word = random.choice(easy_words).upper()
    if level == "M":
        secret_word = random.choice(medium_words).upper()
    if level == "H":
        secret_word = random.choice(hard_words).upper()
    return secret_word


show_word = (choose_difficulty())
print(show_word)


def blanks(word):
    blanks = []
    for _ in word:
        blanks.append("_")
    return blanks


display_word = blanks(show_word)


def get_word(word, guesses):
        # input "alpha",['a', 'l']
        # output: "al__a"
    output_letters = []
    for letter in word:
        if letter in guesses:
            output_letters.append(letter)
        else:
            output_letters.append("_")
    return "".join(output_letters)


def game(show_word):
    printed_word = []
    guesses = 8
    guessed_letters = []
    while guesses > -1:
        input_letter = input("Please guess a letter").upper()
        if input_letter not in show_word:
            guesses = guesses - 1
            guessed_letters.append(input_letter)
            print("Sorry that letter not in the word. You still have ",
                  guesses,  " guesses")

        if input_letter in show_word:
            print("Yes, it's there! You still have ", guesses, " guesses")
            guessed_letters.append(input_letter)

        printed_word = get_word(show_word, guessed_letters)

        if printed_word == show_word:
            print("Yay, you won!")
            break
        if guesses == 0:
            print("Sorry you are out of guesses. The word is ", show_word)
            break
        print("Your guessed letters are ", guessed_letters)
        print(printed_word)


game(show_word)
