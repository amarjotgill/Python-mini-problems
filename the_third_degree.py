"""
File: the_third_degree.py
Author: Amarjot Gill
Date: 10/31/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will return the sequence
using recursion of the number put into the
parameter

"""


# function that does the recursion
def the_third_degree(n):
    # these ifs are the base cases
    if n == 0:
        return 2

    elif n == 1:
        return 1

    elif n == 2:
        return 5
    # this is for the other numbers larger than 2 it will use recursion
    # to return the number in the sequence at n
    elif n > 2:
        number = 3 * the_third_degree(n - 1) + 2 * the_third_degree(n - 2) + the_third_degree(n - 3)
        return number


if __name__ == '__main__':
    for i in range(10):
        print(the_third_degree(i))
