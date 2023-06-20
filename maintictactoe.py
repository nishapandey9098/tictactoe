#tic tac toe
"""
[]: Draw a board
[]: Print a board
[]: Put sign to each player
[]: Ask user to input X or 0
[]: Print board after each input
[]: Calculate and display the result
"""
instructions = """
This will be our tic tac toe board


 1  | 2  | 3  
----|----|----
 4  | 5  | 6  
----|----|----
 7  |  8 | 9  
 
 *INSTRUCTIONS:
 
 1. Insert the spot number (0-9) to put your sign.
 2. You must fill all 9 spots to get the result
 3. "X" will go first.
   """  
def main():
    print ("Welcome to the game of TIC TAC TOE!!!")
    
print (instructions)
main()

def print_board(board):
    """
    Prints the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board):
    
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "Tie"
    return None

def play_tic_tac_toe():
   
    current_player="X"
   
    board = [[" " for _ in range(3)] for _ in range(3)]
    winner = None

    while not winner:
        print_board(board)

        # Get the current player's move
        print(f"Player {current_player}, make your move:")
        position = int(input("Enter the position number (1-9): ")) - 1

        # Validation of move
        row = position // 3
        col = position % 3
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner or tie
        winner = check_winner(board)

        # to switch the players
        current_player= "O" if current_player == "X" else "X"
    print_board(board)

# Print the game result
    if winner == "Tie":
        print("It's a tie!")
        print("WELL PLAYED!!!")
        print("THANK YOU FOR JOINING!!!")
    else:
        print("CONGRATULATIONS!!!!")
        print(f"Player {winner} wins!")
        print("THANK YOU FOR JOINING!!!")
play_tic_tac_toe()
