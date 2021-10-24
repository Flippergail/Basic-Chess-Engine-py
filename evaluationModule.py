# importing packages
import chess
from math import pi


# evaluation classes and functions
class materialEval:
    def __init__(self):
        pass

    def run(self, board):
        eval = 0
        eval += self.actual_weight(board)
        eval += self.rough_position_weight(board)
        eval += self.pawn_shields(board)
        eval += self.passed_pawn(board)
        eval += self.two_bishops(board)
        eval += self.doubled_rooks(board)
        if board.turn:
            return eval
        else:
            return -eval

    def actual_weight(self, board):
        wp = len(board.pieces(chess.PAWN, chess.WHITE))
        bp = len(board.pieces(chess.PAWN, chess.BLACK))
        wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(board.pieces(chess.ROOK, chess.WHITE))
        br = len(board.pieces(chess.ROOK, chess.BLACK))
        wq = len(board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(board.pieces(chess.QUEEN, chess.BLACK))

        eval = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
        return eval

    def rough_position_weight(self, board):
        pawntable = [
            0, 0, 0, 0, 0, 0, 0, 0,
            5, 10, 10, -20, -20, 10, 10, 5,
            5, -5, -10, 0, 0, -10, -5, 5,
            0, 0, 0, 20, 20, 0, 0, 0,
            5, 5, 10, 25, 25, 10, 5, 5,
            10, 10, 20, 30, 30, 20, 10, 10,
            50, 50, 50, 50, 50, 50, 50, 50,
            0, 0, 0, 0, 0, 0, 0, 0]

        knightstable = [
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50]

        bishopstable = [
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 5, 5, 10, 10, 5, 5, -10,
            -10, 0, 5, 10, 10, 5, 0, -10,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -20, -10, -10, -10, -10, -10, -10, -20]

        rookstable = [
            0, 0, 0, 5, 5, 0, 0, 0,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            5, 10, 10, 10, 10, 10, 10, 5,
            0, 0, 0, 0, 0, 0, 0, 0]

        queenstable = [
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 5, 5, 5, 5, 5, 0, -10,
            0, 0, 5, 5, 5, 5, 0, -5,
            -5, 0, 5, 5, 5, 5, 0, -5,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20]

        kingstable = [
            20, 30, 10, 0, 0, 10, 30, 20,
            20, 20, 0, 0, 0, 0, 20, 20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            -20, -30, -30, -40, -40, -30, -30, -20,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30]

        pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
        pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                               for i in board.pieces(chess.PAWN, chess.BLACK)])
        knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
        knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                                   for i in board.pieces(chess.KNIGHT, chess.BLACK)])
        bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
        bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                                   for i in board.pieces(chess.BISHOP, chess.BLACK)])
        rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
        rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                               for i in board.pieces(chess.ROOK, chess.BLACK)])
        queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
        queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                                 for i in board.pieces(chess.QUEEN, chess.BLACK)])
        kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
        kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                               for i in board.pieces(chess.KING, chess.BLACK)])

        eval = pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
        return eval

    def pawn_shields(self, board):
        squares_of_king = list(board.pieces(6, True))
        squares_of_pawn = list(board.pieces(1, True))
        combinations = [[7, 8, 9], [7, 16, 9], [15, 9, 10]]
        new_comb = []
        if (squares_of_king[0] - 1) % 8 == 7 or squares_of_king[0] - 1 == -1:
            combinations = [[8, 9], [16, 9]]
        elif (squares_of_king[0] + 1) % 8 == 0:
            combinations = [[7, 8], [7, 16]]
        for columns in range(len(combinations[0])):
            col = []
            for rows in range(len(combinations[0])):
                col.append(combinations[columns][rows] + int(squares_of_king[0]))
            new_comb.append(col)
        for i in new_comb:
            if set(i) <= set(squares_of_pawn):
                return 80
        return 0

    def passed_pawn(self, board):
        points = 0
        squares_of_pawn_w = list(board.pieces(1, True))
        squares_of_pawn_b = list(board.pieces(1, False))
        for i in range(len(squares_of_pawn_w)):
            passed = True
            if (squares_of_pawn_w[i] - 1) % 8 == 7:
                combinations = [squares_of_pawn_w[i] + 8, squares_of_pawn_w[i] + 9]
            elif (squares_of_pawn_w[i] + 1) % 8 == 0:
                combinations = [squares_of_pawn_w[i] + 7, squares_of_pawn_w[i] + 8]
            else:
                combinations = [squares_of_pawn_w[i] + 7, squares_of_pawn_w[i] + 8, squares_of_pawn_w[i] + 9]
            for j in range(18):
                combinations.append(combinations[j] + 8)
            for f in range(len(combinations)):
                if combinations[f] in squares_of_pawn_b:
                    passed = False
                    break
            if passed:
                points += 15
        return points

    """def isolated_pawn(self, board):
        points = 0
        squares_of_pawn = list(board.pieces(1, True))
        definite_squares_of_pawn = list(board.pieces(1, True))
        x = len(squares_of_pawn)
        if x == 1:
            return -10
        elif x == 0:
            return 0
        for i in range(x):
            isolated = True
            if (squares_of_pawn[i] - 1) % 8 == 7:
                combinations = [squares_of_pawn[i] + 8, squares_of_pawn[i] + 9]
            elif (squares_of_pawn[i] + 1) % 8 == 0:
                combinations = [squares_of_pawn[i] + 7, squares_of_pawn[i] + 8]
            else:
                combinations = [squares_of_pawn[i] + 7, squares_of_pawn[i] + 8, squares_of_pawn[i] + 9]
            for j in range(18):
                combinations.append(combinations[j] + 8)
            for f in range(len(combinations)):
                if combinations[f] in definite_squares_of_pawn:
                    isolated = False
                    break
            if isolated:
                points -= 10
        return points"""

    def two_bishops(self, board):
        if len(list(board.pieces(3, True))) == 2:
            return 12
        else:
            return 0

    """def doubled_pawns(self, board):
        points = 0
        squares_of_pawn = list(board.pieces(1, True))
        if len(squares_of_pawn) == 0 or len(squares_of_pawn) == 1:
            return 0
        for i in range(len(squares_of_pawn)):
            combination = [squares_of_pawn[i] + 8]
            for k in range(6):
                combination.append(combination[k] + 8)
            for f in range(len(combination)):
                if combination[f] in squares_of_pawn:
                    points -= 5
        return points"""

    def doubled_rooks(self, board):
        squares_of_rooks = list(board.pieces(4, True))
        if len(squares_of_rooks) <= 1:
            return 0
        for i in range(len(squares_of_rooks) - 1):
            if squares_of_rooks[i] % 8 == squares_of_rooks[i + 1] % 8:
                return 15
        return 0


# checks if the game ends
def checkGameEnd(board):
    if board.is_checkmate():
        if board.turn:
            return -float("inf")
        else:
            return float("inf")
    if board.is_stalemate(): return 0
    if board.is_fivefold_repetition(): return 0
    if board.is_seventyfive_moves(): return 0
    if board.is_insufficient_material(): return 0
    return pi


# evaluation function
material = materialEval()
def evaluate(board_position):
    bp = board_position
    points = 0
    gameEnd = checkGameEnd(bp)
    if gameEnd != pi: return gameEnd
    points += material.run(bp)
    return points