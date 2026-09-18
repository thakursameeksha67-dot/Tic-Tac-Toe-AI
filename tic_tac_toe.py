
import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()

def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are X. AI is O.")
    print("Choose positions from 1 to 9.")

    while True:
        print_board()

        try:
            position = int(input("Enter your position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Choose a number between 1 and 9.")
                continue

            if board[position] != " ":
                print("That position is already occupied.")
                continue

            board[position] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        result = check_winner()

        if result:
            print_board()
            print("Result:", result)
            break

        ai_move()

        result = check_winner()

        if result:
            print_board()
            print("Result:", result)
            break

play_game()