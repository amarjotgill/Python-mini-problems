"""
File: pickets_file.py
Author: Amarjot Gill
Date:  12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will navigate the 2d list
given and look for pickets. Once it finds a picket it will then
check diagonally too see if this is a legal board.


"""
S = "_"
P = "P"
TWO = 2
ONE = 1


# this function was just so I could display the grid and see the outcomes for testing
def display(the_grid):
    for row in the_grid:
        for x in row:
            if x == S:
                print(S.ljust(3), end=' ')
            else:
                print(P.ljust(3), end=' ')
        print()
    print()


def pickets_problem(board):
    length_of_board = len(board)

    for i in range(len(board)):
        for x in range(len(board)):
            # if the square is a P then it will check diagonally 2 spaces
            if board[i][x] == P:
                # 2 by 2 is the diagonal we start with
                row = TWO
                column = TWO
                works = True
                while works:
                    # checks to make sure diagonal stays within bounds of board
                    if x + column <= length_of_board - ONE and i + row <= length_of_board - ONE:
                        # if the diagonal is another P it will return false
                        if board[i + row][x + column] == P:
                            return False
                        # else it will go to the next diagonal of this P
                        else:
                            row += ONE
                            column += ONE
                    # if the move is no longer within the bounds then the function
                    # will move on
                    else:
                        works = False

    # if it all works true will be returned
    return True


if __name__ == '__main__':
    the_board = [[P, S, S, S, S], [P, P, S, P, S], [S, S, S, S, S], [S, S, S, S, S], [S, S, S, S, P]]
    display(the_board)
    print(pickets_problem(the_board))



