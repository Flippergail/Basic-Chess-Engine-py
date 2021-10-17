# importing packages
import pandas as pd
import numpy as np
from evaluationModule import evaluate
from evaluationModule import checkGameEnd
import chess
from math import pi

board = chess.Board()
runamount = 0
moveNumber = 0

# negamax search


def negaMax(board, depth):
    global runamount
    runamount += 1
    if depth == 0: return evaluate(board)
    max = -float('inf')
    for i, v in enumerate(board.legal_moves):
        board.push(chess.Move.from_uci(str(v)))
        score = -negaMax(board, depth-1)
        board.pop()
        if score > max:
            max = score
    return max


def evalMoves(board, depth):
    global moveNumber
    moveNumber += 1
    if checkGameEnd(board) != pi:
        print("Game Has Ended.")
        print(moveNumber)
        exit()
    my_moves = pd.DataFrame(columns=['score', 'move'])
    my_moves['row_num'] = np.arange(len(list(board.legal_moves)))
    for i, v in enumerate(board.legal_moves):
        board.push(chess.Move.from_uci(str(v)))
        if depth == 0: score = evaluate(board)
        elif checkGameEnd(board) != pi: score = checkGameEnd(board)
        else: score = negaMax(board, depth-1)
        board.pop()
        my_moves.iat[i, 0] = score
        my_moves.iat[i, 1] = str(v)
    best_move = my_moves.loc[my_moves['score'].astype(float).idxmin()]['move']
    return best_move


"""def traverse_func(board, remaining_depth):
    global runamount
    runamount += 1
    remaining_depth -= 1
    my_moves = pd.DataFrame(columns=['score', 'move'])
    my_moves['row_num'] = np.arange(len(list(board.legal_moves)))
    for i, v in enumerate(board.legal_moves):
        board.push(chess.Move.from_uci(str(v)))
        enemy_moves = pd.DataFrame(columns=['score', 'move'])
        enemy_moves['row_num'] = np.arange(len(list(board.legal_moves)))
        for z, k in enumerate(board.legal_move
        s):
            board.push(chess.Move.from_uci(str(k)))
            if remaining_depth == 1:
                print("miss")
                enemy_score = evaluate(board)
            else:
                enemy_score = traverse_func(board, remaining_depth)
            enemy_moves.iat[z, 0] = enemy_score
            enemy_moves.iat[z, 1] = str(k)
            board.pop()
        enemy_row = enemy_moves.loc[enemy_moves['score'].astype(float).idxmax()]
        my_moves.iat[i, 0] = enemy_row['score']
        my_moves.iat[i, 1] = enemy_row['move']
        board.pop()
    return enemy_moves.loc[enemy_moves['score'].astype(float).idxmin()]['move']"""

while not board.is_game_over():
    move = evalMoves(board, 3)
    board.push(chess.Move.from_uci(move))
    print(move)
    print(moveNumber)
    playerMove = input("make a move ")
    if playerMove == "board":
        print(board)
        board.pop()
        board.pop()
        playerMove = input("make a move ")
    board.push(chess.Move.from_uci(playerMove))
    moveNumber += 1
    print(moveNumber)
