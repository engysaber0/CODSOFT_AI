def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_draw(board):
    return is_board_full(board) and check_winner(board) is None

def minimax(board, depth, maximizing_player):
    if check_winner(board) == 'O':  # AI wins
        return 10 - depth
    elif check_winner(board) == 'X':  # Human wins
        return depth - 10
    elif is_draw(board):  # It's a draw
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_value = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_value = minimax(board, 0, False)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

def play_game():
    board = initialize_board()
    human_turn = True

    while True:
        print_board(board)
        if human_turn:
            while True:
                try:
                    move = input("Enter your move (row and column, e.g., '0 0' for the top-left corner): ").split()
                    move = [int(x) for x in move]
                    if len(move) != 2 or not (0 <= move[0] < 3 and 0 <= move[1] < 3):
                        print("Invalid input. Please enter two integers within the range 0 to 2.")
                        continue
                    if board[move[0]][move[1]] != ' ':
                        print("That cell is already taken. Try again.")
                        continue
                    board[move[0]][move[1]] = 'X'
                    break
                except ValueError:
                    print("Invalid input. Please enter two integers separated by space.")
        else:
            move = find_best_move(board)
            board[move[0]][move[1]] = 'O'

        winner = check_winner(board)
        if winner or is_draw(board):
            print_board(board)
            if winner:
                print(f"The winner is {winner}")
            else:
                print("It's a draw!")
            break

        human_turn = not human_turn

play_game()
