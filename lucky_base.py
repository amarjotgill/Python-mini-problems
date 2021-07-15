"""
File: lucky_base.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will take a number to be converted into
it's base 7 number using slicing and simple division and mod.
"""
SEVEN = 7


def lucky_base(number):
    if number == 0:
        return 0
    # will add to this
    base_7_number = ''
    while number:
        # converts the number into a string
        base_7_number += str(number % SEVEN)
        # integer dividing by 7
        number = number // SEVEN
    # number ends up being backwards so this will reverse it
    return base_7_number[::-1]


if __name__ == '__main__':
    what_number = int(input("What number do you want base 7 of?"))

    while what_number < 0:
        print("Only non-negatives are allowed! Reenter")
        what_number = int(input("What number do you want base 7 of?"))

    print(lucky_base(what_number))
