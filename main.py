# importing packages
import pandas as pd
import numpy as np
from evaluationModule import evaluate
from evaluationModule import checkGameEnd
import chess
from math import pi

board = chess.Board()
run_amount = 0
moveNumber = 0

# negamax search


def negamax(board, depth, cutOff):
    global run_amount
    run_amount += 1
    eval_score = evaluate(board)
    if depth == 0 or eval_score < cutOff: return eval_score
    max = -float('inf')
    for i, v in enumerate(board.legal_moves):
        board.push(chess.Move.from_uci(str(v)))
        score = -negamax(board, depth-1, cutOff)
        board.pop()
        if score > max:
            max = score
    return max


def eval_moves(board):
    depth = 4
    if len(list(board.legal_moves)) <= 20:
        depth = 4
    if len(list(board.legal_moves)) <= 130:
        depth = 5
        cutOff = -1000
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
        else: score = negamax(board, depth-1, cutOff)
        board.pop()
        my_moves.iat[i, 0] = score
        my_moves.iat[i, 1] = str(v)
    best_move = my_moves.loc[my_moves['score'].astype(float).idxmin()]['move']
    return best_move


"""while not board.is_game_over():
    move = eval_moves(board)
    board.push(chess.Move.from_uci(move))
    print("\n")
    print(board)"""

while not board.is_game_over():
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
    move = eval_moves(board)
    board.push(chess.Move.from_uci(move))
    print(move)
