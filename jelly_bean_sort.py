"""
File: jelly_bean_sort.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will take a list filled with
jelly bean colors, it will then count the number of each color of
bean within the list and return the list sorted in order.
"""
ONE = 1
ZERO = 0
QUIT = "quit"


def jelly_bean_sort(list_of_colors):
    # this list will separate all of the colors
    color_list = []
    # this list will be the one that gets sorted
    list_to_sort = []
    for color in list_of_colors:
        color_exist = False
        for i in range(len(color_list)):
            # checks if the color was already added to color_list
            if color in color_list[i]:
                color_list[i].append(color)
                color_exist = True
        # creates a new color if one is not already made
        if not color_exist:
            color_list.append([color])
    # this will make it so it's just one color and the amount of that color
    for lists in color_list:
        list_to_sort.append([lists[ZERO], len(lists)])

    # I choose a bubble sort to sort
    for i in range(len(list_to_sort) - ONE):
        for j in range(len(list_to_sort) - ONE):
            # if the thing is out of order
            # checks for the 1 index which is amount of colors for each color
            if list_to_sort[j][ONE] > list_to_sort[j + ONE][ONE]:
                # swaps it
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + ONE]
                list_to_sort[j + ONE] = temp

    return list_to_sort


if __name__ == '__main__':
    jelly_bean_list = []

    bean = input("Enter a color of bean, quit to end!").lower()
    while bean != QUIT:
        jelly_bean_list.append(bean)
        bean = input("Enter a color of bean, quit to end!").lower()    

    print(jelly_bean_sort(jelly_bean_list))
