board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))

def check_winner(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==player for i,j,k in wins)

def minimax(player):
    if check_winner("O"): return 1
    if check_winner("X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            score = minimax("O" if player == "X" else "X")
            scores.append(score)
            board[i] = " "

    return max(scores) if player == "O" else min(scores)

def ai_move():
    best_score = -2
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax("X")
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

def game():
    print("You: X  |  AI: O")
    print_board()
    while True:
        try:
            move = int(input("Your move (0-8): "))
            if board[move] != " ": raise ValueError
            board[move] = "X"
        except:
            print("Invalid move. Try again.")
            continue

        if check_winner("X"):
            print_board()
            print("You win!")
            break
        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if " " not in board:
            print("It's a draw!")
            break

game()
