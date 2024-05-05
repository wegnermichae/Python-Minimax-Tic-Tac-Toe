import math

def main():
    board = make_board()
    print_board(board)

    turn_counter = 0

    while not check_win(board):
        if turn_counter % 2 == 0:
            player = "X"
        else:
            player = "O"
        location = input("Enter a location (1-9) on where to move (Board is top to bottom, left to right): ")
        row,col = switch_case(location)
        valid = check_full(board, row, col)
        if not valid:
            board[row][col] = player
            turn_counter = turn_counter + 1
            print_board(board)
            check_win(board)
            if turn_counter == 9 and not check_win(board):
                print("Tie game!")
                break
            if player == "X":
                print("Best move for 'O' is: ")
                print(reverse_switch(find_best_move(board)))
        else:
            print("Sorry that spot is full. Please enter an empty location.")
    if check_win(board):
        print("Congrates! Player", player)


# Java type switch case method used to turn number input into row and column output
def switch_case(arg):
    if int(arg) == 1:
        row = 0
        col = 0
        return row, col
    if int(arg) == 2:
        row = 0
        col = 1
        return row, col
    if int(arg) == 3:
        row = 0
        col = 2
        return row, col
    if int(arg) == 4:
        row = 1
        col = 0
        return row, col
    if int(arg) == 5:
        row = 1
        col = 1
        return row, col
    if int(arg) == 6:
        row = 1
        col = 2
        return row, col
    if int(arg) == 7:
        row = 2
        col = 0
        return row, col
    if int(arg) == 8:
        row = 2
        col = 1
        return row, col
    if int(arg) == 9:
        row = 2
        col = 2
        return row, col
    
# Java type switch case method used to turn row column input into number output
def reverse_switch(ar):
    if ar == (0,0):
        return 1
    if ar == (0,1):
        return 2
    if ar == (0,2):
        return 3
    if ar == (1,0):
        return 4
    if ar == (1,1):
        return 5
    if ar == (1,2):
        return 6
    if ar == (2,0):
        return 7
    if ar == (2,1):
        return 8
    if ar == (2,2):
        return 9

# Makes board
def make_board():
    row1 = ["-", "-", "-"]
    row2 = ["-", "-", "-"]
    row3 = ["-", "-", "-"]
    board = [row1, row2, row3]
    return board

# Prints board
def print_board(board):
    for b in board:
        print(b)

# Checks if a spot if full and returns true if it is and false if its empty
def check_full(board, row, col):
    if board[row][col] == '-':
        return False
    else:
        return True
    
# checks for a win and returns true if a win is found
def check_win(board):
    for row in board:
        if all(cell == row[0] and cell != "-" and cell for cell in row):
            return True
        
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != '-':
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '-':
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '-':
        return True
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board [2][0] and board[0][2] != '-':
        return True
    


# Evaluate function for minimax
def evaluate(board):
    # Check rows, columns, and diagonals for win or loss
    for symbol in ["X", "O"]:
        if any(all(cell == symbol for cell in row) for row in board) or \
           any(all(board[i][j] == symbol for i in range(3)) for j in range(3)) or \
           all(board[i][i] == symbol for i in range(3)) or \
           all(board[i][2-i] == symbol for i in range(3)):
            return 1 if symbol == "O" else -1

    # If no winner, check for a draw
    if all(board[i][j] != "-" for i in range(3) for j in range(3)):
        return 0  # Draw

    # Game still in progress
    return None
  
# minimax function
def minimax(board, depth, maxi) :  

    result = evaluate(board)

    if result is not None:
        return result

    if maxi:
        MaxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = "-"
                    MaxEval = max(MaxEval, eval)
        return MaxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = "-"
                    minEval = min(minEval, eval)

        return minEval
    
# finds the best move for user 'O' using minimax function
def find_best_move(board):
    bestEval = -math.inf
    bestMove = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = "-"
                if eval > bestEval:
                    bestEval = eval
                    bestMove = (i, j)
    return bestMove


if __name__ == "__main__":
    main()