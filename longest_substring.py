"""
File: longest_substring.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will take two strings
a total_string and a sub string, then using slicing
it will find the longest sub string within find_string
that is also in total_string.
"""
# magical values
ZERO = 0
NEGATIVE_ONE = -1
ONE = 1


def longest_substring(total_string, find_string):
    # this loop will split up total_string
    for x in range(len(total_string), ZERO, NEGATIVE_ONE):
        for w in range(len(total_string) - x + ONE):
            # this will check using slicing if the sliced part matches any strings in find_string
            if total_string[w: w + x] in find_string:
                # sets the largest_count equal to x which will equal the length
                # of the longest sub string
                longest_count = x
                return longest_count


if __name__ == '__main__':
    total_string1 = input("Enter the string")
    string_to_find = input("Enter the string you want to find")

    print(longest_substring(total_string1, string_to_find))
