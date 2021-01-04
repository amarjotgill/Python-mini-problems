"""
File: rota_fortunae.py
Author: Amarjot Gill
Date: 10/4/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will ask for a word the players must guess
then will ask for letters in the program and will
keep going until all letters are guessed
or "solve" is equal too the word.
"""
if __name__ == '__main__':
    word_to_guess = input("What is the word you want the players to guess?")
    length = 0
    list_of_letters = list(word_to_guess)
    # this list is what stores the guess the user must make
    guess = []
    # this will keep track of previous guessed letters
    guessed_before = []
    # this will be used for the user too solve
    solved = []
    # alphabet is here to append _ for letters and nothing for spaces
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    UPPER_ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # loop too append _ for letters and for spaces
    for i in range(len(list_of_letters)):
        if list_of_letters[i] in alphabet or list_of_letters[i] in UPPER_ALPHA:
            guess.append("_")
        else:
            guess.append(" ")
    # will print without spaces in between the _'s
    print(''.join(guess))
    solve_or_guess = input("Guess a letter, or \"solve\"")

    if solve_or_guess == "solve":
        solve = input("What is the entire puzzle?")
        if solve == word_to_guess:
            solved = list(solve)
        elif solve != word_to_guess:
            print("Sorry that is not correct, keep going!")
    else:
        length = len(solve_or_guess)
        if length != 1:
            print("Only 1 letter at a time")
        elif solve_or_guess in guessed_before:
            print("You have already guessed this before")
        else:
            for i in range(len(list_of_letters)):
                # will append both upper and lower case instances of any correct letter
                if solve_or_guess.lower() in list_of_letters[i]:
                    guess[i] = solve_or_guess.lower()
                elif solve_or_guess.upper() in list_of_letters[i]:
                    guess[i] = solve_or_guess.upper()
                    # appends the letter into the index where it belongs in the word
                    guessed_before.append(solve_or_guess)
            """
             will check if both lower and uppercase are not in the list of letters to guess
             and then put them in the guessed before list to keep track of what has been 
             guessed before
            """
            if solve_or_guess.upper() not in list_of_letters \
                    and solve_or_guess.lower() not in list_of_letters:
                print("There are no", solve_or_guess + "'s in the word/phrase ")
                guessed_before.append(solve_or_guess)
            # will print the list with up to date letters
            print(''.join(guess))

    # will keep going unless "solved" or the guess is equal to the list_of_letters
    while guess != list_of_letters and solved != list_of_letters:
        # everything within the while loop runs exactly like loops and ifs
        # outside of the while loop
        solve_or_guess = input("Guess a letter, or \"solve\"")

        if solve_or_guess == "solve":
            solve = input("What is the entire puzzle?")
            if solve == word_to_guess:
                solved = list(solve)
            elif solve != word_to_guess:
                print("Sorry that is not correct, keep going!")
        else:
            length = len(solve_or_guess)

        # will check to make sure only 1 letter at a time
        if length != 1:
            print("Only 1 letter at a time")
        elif solve_or_guess in guessed_before:
            print("You have already guessed this before")
        else:
            for i in range(len(list_of_letters)):
                if solve_or_guess.lower() in list_of_letters[i]:
                    guess[i] = solve_or_guess.lower()
                elif solve_or_guess.upper() in list_of_letters[i]:
                    guess[i] = solve_or_guess.upper()
                    guessed_before.append(solve_or_guess)

            if solve_or_guess.upper() not in list_of_letters \
                    and solve_or_guess.lower() not in list_of_letters:
                print("There are no", solve_or_guess + "'s in the word/phrase ")
                guessed_before.append(solve_or_guess)
            print(''.join(guess))

    print("You solved the puzzle!")