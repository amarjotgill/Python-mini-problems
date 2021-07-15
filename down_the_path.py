"""
File: down_the_path.py
Author: Amarjot Gill
Date: 10/31/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will return the number
of steps taken that the program did to reach a
return of 0 using recursion

"""


def down_the_path(n):

    """

    :param n: an integer
    :return: the number of times that all_the_way_down runs

    """
    # base case
    if n <= 0:
        return 0
    # if it is divisible by any of these 3 it will divide and return the function
    elif n % 15 == 0:
        n = n // 15
        return down_the_path(n) + 1
    elif n % 5 == 0:
        n = n // 5
        return down_the_path(n) + 1
    elif n % 3 == 0:
        n = n // 3
        return down_the_path(n) + 1

    else:
        # if it is even and not divisible it will subtract from the count and return
        if n > 0:
            return down_the_path(n - 1) + 1


if __name__ == '__main__':

    for i in range(20):
        print(i, down_the_path(i))
