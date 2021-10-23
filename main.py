# importing packages
import pandas as pd
import numpy as np
from evaluationModule import miniEvaluate
from evaluationModule import evaluate

import chess.polyglot
from evaluationModule import checkGameEnd
import chess
movehistory = []

board = chess.Board()
moveNumber = 0


def quiesce(alpha, beta, depthLeft):
    stand_pat = evaluate(board)
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat
    if depthLeft == 0:
        return stand_pat

    for i in board.legal_moves:
        if board.is_capture(i) or board.is_game_over():
            board.push(i)
            score = -quiesce(-beta, -alpha, depthLeft-1)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    return alpha


def alphabeta(alpha, beta, depthleft):
    max = -float("inf")
    if depthleft == 0:
        return quiesce(alpha, beta, 2)
    for i in board.legal_moves:
        board.push(i)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if score >= beta:
            return score
        if score > max:
            max = score
        if score > alpha:
            alpha = score
    return max


def selectmove():
    depth = 4
    """try:
        move = chess.polyglot.MemoryMappedReader("Perfect2017-SF12.bin").weighted_choice(board)
        movehistory.append(move)
        return move
    except:"""
    bestMove = chess.Move.null()
    bestValue = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabeta(-beta, -alpha, depth-1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        board.pop()
        movehistory.append(bestMove)
    return bestMove


"""def eval_moves(board):
    depth = 4
    legal_moves_list = list(board.legal_moves)
    if len(board.pieces) <= 6:
        depth += 1
    global moveNumber
    moveNumber += 1
    if checkGameEnd(board) != pi:
        print("Game Has Ended.")
        print(moveNumber)
        exit()
    my_moves = pd.DataFrame(columns=['score', 'move'])
    my_moves['row_num'] = np.arange(len(legal_moves_list))
    for i, v in enumerate(legal_moves_list):
        board.push(chess.Move.from_uci(str(v)))
        if depth == 0: score = evaluate(board)
       # elif checkGameEnd(board) != pi: score = checkGameEnd(board)
        else: score = negamax(board, depth-1)
        board.pop()
        my_moves.iat[i, 0] = score
        my_moves.iat[i, 1] = str(v)
    best_move = my_moves.loc[my_moves['score'].astype(float).idxmin()]['move']
    return best_move"""


"""while not board.is_game_over():
    moveNumber += 1
    move = selectmove()
    board.push(chess.Move.from_uci(str(move)))
    print("\n")
    print(board)
    #print(str(moveNumber), move)
print("game finished")
if board.is_checkmate():
    if board.turn:
        print("white won with checkmate")
    else:
        print("black won with checkmate")"""

while not board.is_game_over():
    move = str(selectmove())
    board.push(chess.Move.from_uci(move))
    print(move)
    try:
        playerMove = input("make a move ")
        if playerMove == "board":
            print(board)
            board.pop()
            board.pop()
            playerMove = input("make a move ")
        board.push(chess.Move.from_uci(playerMove))
    except:
        playerMove = input("make a move ")
        if playerMove == "board":
            print(board)
            board.pop()
            board.pop()
            playerMove = input("make a move ")
        board.push(chess.Move.from_uci(playerMove))
    moveNumber += 1