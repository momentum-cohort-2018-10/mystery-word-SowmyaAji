# import random


# def game_begins():


# play_again = True


# def game_level():
#             """Given the input, take the game to the right level"""

#         if g_l == "e":
#             print("yes, let's try it!")
#         elif g_l == "m":
#             print("I like your confidence, let's go!")
#         elif g_l == "h":
#             print("awesome. Let's kill it!")
#         else:
#             print(
#                 "hey, I don't understand. Will you please type one of these three letters -- E, M or H? And we could go rock!")
#             game_level()
#         return whatever_input
# difficulty = game_level(g_l)


# def word_dict():
#     words_e_level = []
#     words_m_level = []
#     words_h_level = []

#     with open('words.txt') as dictionary_file:
#     for word_to_use in dictionary_file.readlines():
#         if len(word_to_use) >= 4 and len(word_to_use) <= 6:
#             words_e_level.append(word_to_use.strip())
#         if len(word_to_use) >= 6 and len(word_to_use) <= 8:
#             words_m_level.append(word_to_use.strip())
#         if len(word_to_use) > 8:
#                     words_h_level.append(word_to_use.strip())

# def

#     while play_again:


#         g_l = input("Welcome to Mystery Word! Let's have fun as we pick a word for you to guess, letter by letter. What level would you like to play? For easy, type E; for medium type M; or if you want to try hard, type H!").lower()


#         with open('words.txt') as dictionary_file:

#             for word_to_use in dictionary_file.readlines():

#             # print(random.choice(words_h_level))

#         def word_to_guess(difficulty):
#             """Given a choice of level by user, pick a random word from the appropriate list of words"""

#             if difficulty == "e":
#                 return(random.choice(words_e_level))

#             elif difficulty == "m":
#                 return(random.choice(words_m_level))

#             elif difficulty == "h":
#                 return(random.choice(words_h_level))

#         def number_of_blanks(show_word):
#             """Given a random word picked for the level inputed, display an equal number of blanks for it """
#             word_blanks = []
#             print(chosen_word)
#             for _ in show_word:
#                 word_blanks.append("_")
#             return word_blanks

#         chosen_word = word_to_guess(difficulty)
#         # print (chosen_word)
#         print(number_of_blanks(chosen_word))

#         input_letter = input(
#             "Here is your mystery word! You have eight guesses to get it right! Press enter to start playing!")
#         guessed_letters = []
#         remaining_guesses = 8

# import random


# def print_word(word, guesses):
#         # input "alpha",['a', 'l']
#         # output: "al__a"
#     output_letters = []
#     for letter in word:
#         if letter in guesses:
#             output_letters.append(letter)
#         else:
#             output_letters.append("_")
#     return " ".join(output_letters)


# response_to_print = print_word(chosen_word, input_letter)

#         while response_to_print != chosen_word or remaining_guesses > 0 or remaining_guesses <= 8:
#             input_letter = input("What letter do you want to guess?")
#             guessed_letters.append(input_letter)
#             print(input_letter)
#             print(guessed_letters)
#             print(chosen_word)
#             response_to_print = print_word(chosen_word, guessed_letters)
#             print(response_to_print)

#             if response_to_print == chosen_word:
#                 print("You won!")
#                 break

#             if input_letter not in chosen_word:
#                 remaining_guesses = remaining_guesses - 1
#                 print("Awww you got that wrong! Try again. You still have",
#                       remaining_guesses, "guesses!")
#                 print("The letters you've picked so far are:", guessed_letters)

#             elif input_letter in chosen_word:
#                 print("Yessss!! It's there. And, you still have",
#                       remaining_guesses, "guesses!")
#                 print("The letters you've picked so far are:", guessed_letters)

#             response_to_print = print_word(chosen_word, guessed_letters)
#             print(response_to_print)

#             if remaining_guesses == 0:
#                 print("Tough luck! The word was", chosen_word)

#         ask_again = input(
#             "Do you want to play again? Take a shot! Type Y for yes or N for no: ").lower()

#         if ask_again == "n":

#             print(
#                 "Hey, we are sorry to see you go! Take heart and come back soon! Bye for now!")

#             play_again = False


# game_begins()

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
