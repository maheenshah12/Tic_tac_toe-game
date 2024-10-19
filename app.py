streamlit run tic_tac_toe.py





# Tic-Tac-Toe Game in Python for Google Colab

# Function to print the game board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    return " " not in board

# Function to play the Tic-Tac-Toe game
def play_game():
    # Initialize the game board with empty spaces
    board = [" "] * 9
    current_player = "X"  # Player "X" starts first

    # Loop until there's a winner or the game is a draw
    while True:
        print_board(board)
        
        # Ask the current player for their move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
            else:
                print("Invalid move! The spot is already taken.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
