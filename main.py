import numpy as np
import random


class Player:
    name = ""
    char = ""

    def __init__(self, name, char):
        self.name = name
        self.char = char
        return


def main():
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    print("Welcome to Tic-Tac-Toe.")
    players = list(get_player_names())
    random.shuffle(players)
    player_1 = Player(players.pop(), "X")
    player_2 = Player(players.pop(), "O")

    while True:
        print(f"\n{player_1.name}'s go.")
        print_board(board)
        add_to_board(player_1, board)
        print_board(board)
        winner = check_for_winner(board)
        if winner[0] is not False:
            print(f"\n{winner[1]} has won the game")
            return

        print(f"\n{player_2.name}'s go.")
        print_board(board)
        add_to_board(player_2, board)
        print_board(board)
        winner = check_for_winner(board)
        if winner[0]:
            print(f"\n{winner[1]} has won the game")
            return


def check_for_winner(board):
    # Check rows
    for row in board:
        if any(elem == "" for elem in row):
            continue
        if len(set(row)) == 1:
            return True, row[0]

    # Check cols
    for col in np.transpose(board):
        if any(elem == "" for elem in col):
            continue
        if len(set(col)) == 1:
            return True, col[0]

    # Check diagonals
    diagonal_1 = [board[i][i] for i in range(len(board))]
    diagonal_2 = [board[i][len(board) - i - 1] for i in range(len(board))]
    if not any(ele == "" for ele in diagonal_1):
        if len(set(diagonal_1)) == 1:
            return True, board[1][1]
    if not any(ele == "" for ele in diagonal_2):
        if len(set(diagonal_2)) == 1:
            return True, board[1][1]

    return False, ""


def get_player_names():
    player_1 = input("Enter the name of player 1: ")
    player_2 = input("Enter the name of player 2: ")

    return player_1, player_2


def print_board(board):
    for i, row in reversed(list(enumerate(board))):
        print(f"{i}  ", end="")
        for char in row:
            if char == "":
                print(f"|   ", end="")

            else:
                print(f"| {char} ", end="")

        print("|")

    for i in range(len(board)):
        print(f"\t {i} ", end="")


def add_to_board(Player, board):
    move = input(f"\n{Player.name}, where would you like to place? [Format : 'X Y']")

    while int(move.split(' ')[1]) >= len(board) \
            or int(move.split(' ')[1]) < 0 \
            or int(move.split(' ')[0]) >= len(board[0]) \
            or int(move.split(' ')[0]) < 0 \
            or board[int(move.split()[1])][int(move.split()[0])] != "":
        move = input(f"\nInvalid Input, please try again! [Format : 'X Y']")

    coords = move.split(' ')
    board[int(coords[1])][int(coords[0])] = Player.char


if __name__ == '__main__':
    main()
