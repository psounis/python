from random import randrange, seed
from datetime import datetime

# globals
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# functions

def print_board():
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")


def check_row(row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2]) and board[row][0] != " "


def check_col(col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col]) and board[0][col] != " "


def check_diagonals():
    return ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ") or \
           (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != " "


def computer_moves(level):
    def danger_sequence(sequence):
        xs = 0
        empty = None
        for sq in sequence:
            if board[sq[0]][sq[1]] == "X":
                xs += 1
            elif board[sq[0]][sq[1]] == " ":
                empty = sq

        if xs == 2 and empty is not None:
            return empty
        return None

    def danger():
        for i in range(3):
            row = [(i,j) for j in range(3)]
            sq = danger_sequence(row)
            if sq is not None:
                return sq

        for j in range(3):
            col = [(i,j) for i in range(3)]
            sq = danger_sequence(col)
            if sq is not None:
                return sq

        sq = danger_sequence([(0,0),(1,1),(2,2)])
        if sq is not None:
            return sq

        sq = danger_sequence([(0,2),(1,1),(2,0)])
        if sq is not None:
            return sq


    if level == 1:
        squares = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    squares += [(i,j)]

        return squares[randrange(len(squares))]

    else: # hard
        sq = danger()
        if sq is not None:
            return sq
        elif board[1][1] == " ":
            return (1,1)
        else:
            corner_squares = [(0,0), (0,2), (2,0), (2,2)]
            empty_squares = []
            for sq in corner_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]

            middle_squares = [(0,1), (1,0), (1,2), (2,1)]
            empty_squares = []
            for sq in middle_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]


def main():
    seed(datetime.now())
    level = int(input("Choose level(1-easy, 2-hard): "))

    player = "O"
    for _ in range(9):
        print_board()

        # choose next player
        if player == "X":
            player = "O"
        else:
            player = "X"

        # user input
        while player == "X":
            print("Player " + player + " plays! ")
            row = int(input("Give row: "))
            col = int(input("Give column: "))
            if row < 0 or row > 2:
                print("Row out of bounds (0-2). ")
                continue
            elif col < 0 or col > 2:
                print("Column out of bounds (0-2). ")
                continue
            elif board[row][col]!=" ":
                print("Pick an empty box")
                continue
            else:
                board[row][col]=player
                break
        if player == "O":
            sq = computer_moves(level)
            board[sq[0]][sq[1]] = "O"

        # check winner
        winner = False

        for i in range(3):
            if check_row(i):
                winner = player
                break
            if check_col(i):
                winner = player
                break
        if not winner:
            if check_diagonals():
                winner = player

        if winner:
            print_board()
            print("Player " + player + " won! ")
            break

    else:
        print_board()
        print("Draw! ")


# main

main()