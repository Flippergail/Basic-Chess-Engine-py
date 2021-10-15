# importing packages
import numpy as np
import random as ran
import chess

board = chess.Board()
#if board.is_checkmate() or board.is_stalemate() or board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_insufficient_material():
# evaluation function
def negaMax(depth):
    if depth == 0:
        return evaluatePos(depth)
def move