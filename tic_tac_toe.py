def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    winner = None

    while not winner and not is_board_full(board):
        print_board(board)
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

play_game()
