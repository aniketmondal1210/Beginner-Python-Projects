import random
import time

COMPUTER = 1
HUMAN = 2
SIDE = 3  # Board size
COMPUTER_MOVE = 'O'
HUMAN_MOVE = 'X'

def show_board(board):
    print("\n")
    for i in range(SIDE):
        print("\t\t\t", end="")
        for j in range(SIDE):
            print(board[i][j], end=" | " if j < SIDE - 1 else "")
        print()
        if i < SIDE - 1:
            print("\t\t\t" + "-" * 13)
    print()

def show_instructions():
    print("\t\t\tTic-Tac-Toe\n")
    print("Choose a cell numbered from 1 to 9 as below and play:\n")
    print("\t\t\t 1 | 2 | 3 ")
    print("\t\t\t-------------")
    print("\t\t\t 4 | 5 | 6 ")
    print("\t\t\t-------------")
    print("\t\t\t 7 | 8 | 9 \n")
    print("-" * 50 + "\n")

def initialise():
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    moves = list(range(SIDE * SIDE))
    random.shuffle(moves)
    return board, moves

def declare_winner(winner):
    if winner == COMPUTER:
        print("COMPUTER has won\n")
    else:
        print("HUMAN has won\n")

def row_crossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
    return False

def column_crossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    return False

def diagonal_crossed(board):
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def game_over(board):
    return row_crossed(board) or column_crossed(board) or diagonal_crossed(board)

def play_tic_tac_toe(whose_turn):
    board, moves = initialise()
    show_instructions()
    move_index = 0

    while not game_over(board) and move_index < SIDE * SIDE:
        x = moves[move_index] // SIDE
        y = moves[move_index] % SIDE

        if whose_turn == COMPUTER:
            board[x][y] = COMPUTER_MOVE
            print(f"COMPUTER has put a {COMPUTER_MOVE} in cell {moves[move_index] + 1}")
            whose_turn = HUMAN
        else:
            board[x][y] = HUMAN_MOVE
            print(f"HUMAN has put a {HUMAN_MOVE} in cell {moves[move_index] + 1}")
            whose_turn = COMPUTER

        show_board(board)
        move_index += 1
        time.sleep(1)

    if not game_over(board):
        print("It's a draw\n")
    else:
        # Toggle turn to declare the winner correctly
        winner = HUMAN if whose_turn == COMPUTER else COMPUTER
        declare_winner(winner)

if __name__ == "__main__":
    play_tic_tac_toe(COMPUTER)
