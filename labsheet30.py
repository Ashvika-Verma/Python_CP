def evaluate(board):
    # simple evaluation for Tic-Tac-Toe
    for row in board:
        if row.count('X') == 3:
            return 10
        if row.count('O') == 3:
            return -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return 10 if board[0][col] == 'X' else -10
    
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 10 if board[0][0] == 'X' else -10
    
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 10 if board[0][2] == 'X' else -10
    
    return 0


def moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False


def get_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                moves.append((i, j))
    return moves


def make_move(board, move, player):
    i, j = move
    board[i][j] = player


def undo_move(board, move):
    i, j = move
    board[i][j] = '_'