"""
File: nth_day.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will use recursion in order to count
the number of presents received up to that day. It does this by starting at the entered day,
finding out how many presents are received and then using recursion goes to the day before it
all the way to day 0.
"""

ZERO = 0


# count=0 is too keep track of all the presents
def nth_day_of_christmas(day, count=0):
    # when it gets to day 0 it will just return the new count
    if day == ZERO:
        return count

    else:
        # adds to count using the formula
        count += (day * (day + 1)) // 2
        # returns one less day
        return nth_day_of_christmas(day - 1, count)


if __name__ == '__main__':
    the_day = int(input("what day would u like?"))
    while the_day < ZERO:
        print("Please enter only non-negative numbers")
        int(input("what day would u like?"))

    print(nth_day_of_christmas(the_day))





