# importing packages
import pandas as pd
import numpy as np
from evaluationModule import evaluate
from math import pi

import chess.polyglot
from evaluationModule import checkGameEnd
import chess
movehistory = []

board = chess.Board()
moveNumber = 0


def quiesce(alpha, beta, depthLeft):
    stand_pat = evaluate(board)
    gameEnd = checkGameEnd(board)
    if gameEnd != pi: return gameEnd
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
        return quiesce(alpha, beta, 3)
    for i in board.legal_moves:
        gameEnd = checkGameEnd(board)
        if gameEnd != pi: return gameEnd
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
    if checkGameEnd(board) != pi:
        exit("gameEnded")
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

        if checkGameEnd(board) != pi:
            boardValue = checkGameEnd(board)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        board.pop()
        movehistory.append(bestMove)
    return bestMove


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