"""
File: jumble.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will take a string and the offsets to jumble
it by. It will then follow the formula and jumble it. No letter at the same index will be repeated.
"""


def jumble(a_string, a, b):
    l = len(a_string)
    # new string being made
    new_string = ''
    # make sures index is not repeated
    already_used = []
    for i in range(len(a_string)):
        # formula to jumble
        letter = ((a * i) + b) % l
        # checks to make sure the letter index has not already been used
        if letter not in already_used:
            # adds to already used list
            already_used.append(letter)
            # adds to the new word
            new_string += a_string[letter]

    return new_string


if __name__ == '__main__':
    string = input("Enter the string you want to jumble:")
    number_a = int(input("Enter the number you want for a:"))

    while number_a < 0:
        print("Only non-negative numbers are allowed please reenter")
        number_a = int(input("Enter the number you want for a:"))

    number_b = int(input("Enter the number you want for b:"))
    while number_b < 0:
        print("Only non-negative numbers are allowed please reenter")
        number_b = int(input("Enter the number you want for b:"))

    print(jumble(string, number_a, number_b))

