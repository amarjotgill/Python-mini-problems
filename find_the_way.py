"""
File: find_the_way.py
Author: Amarjot Gill
Date: 11/16/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will use recursion to check
and see if their exist a way to exit the map from the starting location,
it will keep track of places it has move with "x"
"""


import sys
import random

ALLOWED = '_'
FORBIDDEN = '*'
BAD = "b"
valid_move = "x"


def create_map(x, y, p):
    """
    :param x: the number of rows of the grid
    :param y: the number of cols of the grid
    :param p: the probability of a forbidden space
    :return: the grid, the starting location
    """
    the_grid = [[FORBIDDEN if random.random() < p else ALLOWED for j in range(y)] for i in range(x)]
    x = random.randint(0, x - 1)
    y = random.randint(0, y - 1)
    the_grid[x][y] = 's'
    return the_grid, [x, y]


def find_the_way_out(the_grid, starting_position):
    """
    :param the_grid: this is a 2d grid, either the positions will be ALLOWED which is a space, or "*" or "s".  s is the starting position passed as a list
        and * is
    :param starting_position:  the starting list/tuple coordinate for the starting position.
    :return: True if there is a way out, False if not

    You need to implement this function
    You are permitted to add helper functions but you shouldn't change the signature (name and parameters) of this function.
    """
    x, y = starting_position
    the_grid[x][y] = valid_move
    # these are the base cases and if the position is on one of the edges
    # of the map this means the program was able to find a way out
    if x == 0:
        return True
    if y == 0:
        return True
    if x == len(the_grid) - 1:
        return True
    if y == len(the_grid) - 1:
        return True
    # go up
    if x - 1 >= 0 and the_grid[x - 1][y] in [ALLOWED]:
        if find_the_way_out(the_grid, (x - 1, y)):
            return True
        the_grid[x - 1][y] = BAD
    # if not then go left
    if y - 1 >= 0 and the_grid[x][y - 1] in [ALLOWED]:
        if find_the_way_out(the_grid, (x, y - 1)):
            return True
        the_grid[x][y - 1] = BAD
    # if not then go right
    if y + 1 < len(the_grid[x]) and the_grid[x][y + 1] in [ALLOWED]:
        if find_the_way_out(the_grid, (x, y + 1)):
            return True
        the_grid[x][y + 1] = BAD
    # else go down
    if x + 1 < len(the_grid) and the_grid[x + 1][y] in [ALLOWED]:
        if find_the_way_out(the_grid, (x + 1, y)):
            return True
        the_grid[x + 1][y] = BAD

    return False


def display(the_grid):
    """
        This should display the grid on the screen.
    :param the_grid: the 2d grid.
    """
    print('\n'.join(''.join([str(x).ljust(3) for x in the_grid[i]]) for i in range(len(the_grid))))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        seed = int(sys.argv[1])
        x_dimension = int(sys.argv[2])
        y_dimension = int(sys.argv[3])
        probability = float(sys.argv[4])
    else:
        seed = input('What is the seed (enter a string): ')
        x_dimension = int(input('Enter the x dimension: '))
        y_dimension = int(input('Enter the y dimension: '))
        probability = float(input('Enter a float between 0 and 1 to represent the probability of a forbidden space: '))

    random.seed(seed)

    while input('Again? ').strip().lower() == 'yes':
        the_grid, starting = create_map(x_dimension, y_dimension, probability)
        display(the_grid)
        print(find_the_way_out(the_grid, starting))
        display(the_grid)
