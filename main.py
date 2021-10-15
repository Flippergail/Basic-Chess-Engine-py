# importing packages
import pandas as pd
import numpy as np
import random
import chess

board = chess.Board()
#if board.is_checkmate() or board.is_stalemate() or board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_insufficient_material():
# evaluation function
def evaluate(board_position):
    bp = board_position
    points = random.randint(1, 10)
    return points

# tree traversing function
def traverse_func(board, remaining_depth):
    if remaining_depth == 0:
        my_moves = pd.DataFrame(data={'score', 'move'})
        for i, v in enumerate(list(board.legal_moves)):
            board.push(chess.Move.from_uci(str(v)))
            enemy_moves = pd.DataFrame([[0, 0]], columns=['score', 'move'])
            print(enemy_moves)
            for z, k in enumerate(list(board.legal_moves)):
                board.push(chess.Move.from_uci(str(k)))
                score = evaluate(board)
                enemy_moves.iat[z, 0] = score
                enemy_moves.iat[z, 1] = str(k)
                board.pop()
            board.pop()
            print(enemy_moves)
traverse_func(board, 0)