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


def main():
    player = "O"

    for _ in range(9):
        print_board()

        # choose next player
        if player == "X":
            player = "O"
        else:
            player = "X"

        # user input
        while True:
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
        print("Isopalia! ")


# main

main()