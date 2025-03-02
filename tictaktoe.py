# Tic-Tac-Toe Game in Python(p1)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    turns = 0

    while turns < 9:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        row, col = map(int, input(
            "Enter row and column (0-2) separated by space: ").split())

        if board[row][col] != " ":
            print("Cell already taken, try again!")
            continue

        board[row][col] = current_player
        turns += 1

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")


game()
