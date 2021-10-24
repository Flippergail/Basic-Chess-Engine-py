def rook_on_second_rank(self, board):
    points = 0
    square_of_rook = list(board.pieces(4, True))
    for i in range(len(square_of_rook)):
        if board.turn and square_of_rook[i] in [55, 54, 53, 52, 51, 50, 49, 48]:
            points += 10
    square_of_rook = list(board.pieces(4, False))
    for i in range(len(square_of_rook)):
        if square_of_rook[i] in [8, 9, 10, 11, 12, 13, 14, 15]:
            points -= 10
    return points

def rooks_on_open_file(self, board):
    squares_of_rooks = list(board.pieces(4, True))
    if len(squares_of_rooks) == 0:
        return 0
    all_other_pieces = []
    List = []
    points = 0
    for i in range(6):
        for j in range(len(list(board.pieces(i + 1, True)))):
            List = list(board.pieces(i + 1, True))
            all_other_pieces.append(List[j])
        for j in range(len(list(board.pieces(i + 1, False)))):
            List = list(board.pieces(i + 1, False))
            all_other_pieces.append(List[j])
    for p in range(len(squares_of_rooks)):
        combinations = [squares_of_rooks[p] + 8]
        for k in range(7):
            combinations.append(combinations[k] + 8)
        for h in range(len(combinations)):
            if combinations[h] > 63:
                break
            if combinations[h] not in all_other_pieces:
                points += 1
            elif combinations[h] in all_other_pieces:
                break
    return points