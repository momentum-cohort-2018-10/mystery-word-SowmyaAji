

def game_begins ():


    play_again = True

    while play_again:

        game_level = input("Welcome to Mystery Word! Let's have fun as we pick a word for you to guess, letter by letter. What level would you like to play? For easy, type E; for medium type M; or if you want to try hard, type H!").lower()

        def correct_syntax(whatever_input):
                """Given an input, ensure that only the correct input works"""
                
                if whatever_input == "e":

                    print("yes, let's try it!")
                
                elif whatever_input == "m":

                    print("I like your confidence, let's go!")

                elif whatever_input == "h":

                    print("awesome. Let's kill it!")

                elif whatever_input != "e" or "m" or "h":

                    print("hey, I don't understand. Will you please type one of these three letters -- E, M or H? And we could go rock!")             
                    
                                 
                        
        correct_syntax(game_level)



        import random
        # def open_dict (lookup_word):

        dictionary_file = open('words.txt')
            # print(repr(dictionary.readlines()))



        words_e_level = []

        with open('words.txt') as dictionary_file:

            for word_to_use in dictionary_file.readlines():
                if len(word_to_use) > 3 and len(word_to_use) < 7:
                    words_e_level.append(word_to_use.strip())


        words_m_level = []

        with open('words.txt') as dictionary_file:
                
            for word_to_use in dictionary_file.readlines():
                if len(word_to_use) > 6 and len(word_to_use) < 8:
                    words_m_level.append(word_to_use.strip())
            # print(random.choice(words_m_level))

        words_h_level = []

        with open('words.txt') as dictionary_file:
                
            for word_to_use in dictionary_file.readlines():
                if len(word_to_use) > 8:
                        words_h_level.append(word_to_use.strip())
            # print(random.choice(words_h_level))

        def word_to_guess():
            """Given a choice of level by user, pick a random word from the appropriate list of words"""

            if game_level == "e":
                return(random.choice(words_e_level))

            elif game_level == "m":
                return(random.choice(words_m_level))

            elif game_level == "h":
                return(random.choice(words_h_level))



        def number_of_blanks(show_word):
            """Given a random word picked for the level inputed, display an equal number of blanks for it """
            word_blanks = []   
            for char in show_word:
                word_blanks.append("_")
            return word_blanks   

        chosen_word = word_to_guess()
            # print (chosen_word)
        print(number_of_blanks(chosen_word))
  

        input_letter = input("Here is your mystery word! You have eight guesses to get it right! Press enter to start playing!")
        guessed_letters = []     
        remaining_guesses = 8    


        def print_word(word, guesses):
                # input "alpha",['a', 'l']
                # output: "al__a"
            output_letters = []
            for letter in word:
                if letter in guesses:
                    output_letters.append(letter)
                else:
                    output_letters.append("_")
            return " ".join(output_letters)
                             
        response_to_print = print_word(chosen_word, input_letter)
            
        while response_to_print != chosen_word and remaining_guesses > 0 and remaining_guesses <=8:
                
            input_letters = input("What letter do you want to guess?")
            guessed_letters.append(input_letters)
            if not input_letters in chosen_word:
                remaining_guesses = remaining_guesses- 1
                print("Awww you got that wrong! Try again. You still have",remaining_guesses, "guesses!")
                print("The letters you've picked so far are:", guessed_letters, "Careful! Don't use them again, you will lose guesses!")
            
            else:  
                print("Yessss!! It's there. And, you still have", remaining_guesses, "guesses!")
                print("The letters you've picked so far are:", guessed_letters)
                
                 
            response_to_print = print_word(chosen_word, guessed_letters)    
            print(response_to_print)


        if remaining_guesses == 0:
            print("Tough luck! The word was", chosen_word)
        else:
            print("Yay, fantastic!")
       
        ask_again = input("Do you want to play again? Take a shot! Type Y for yes or N for no: ").lower()

        if ask_again == "n":
            
            print("Hey, we are sorry to see you go! Take heart and come back soon! Bye for now!")
    
            play_again = False
                

game_begins()



