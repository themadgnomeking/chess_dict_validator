#in this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 5h': 'bqueen', '3e': 'wking'}
#Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid
#A valid board will have exactly 1 black king, and exactly one white king.
#Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space
#from '1a' to '8h'; this is, a piece can't be on space '9z'.
#The piece names begin with either a 'w' or 'b' to represent white or black
#followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chess board

board1 = {'a1': 'wrook', 'a2': 'wpawn', 'a7': 'bpawn', 'a8': 'brook',
'b1': 'wknight', 'b2': 'wpawn', 'b7': 'bpawn', 'b8': 'bknight',
'c1': 'wbishop', 'c2': 'wpawn', 'c7': 'bpawn', 'c8': 'bbishop',
'd1': 'wqueen', 'd2': 'wpawn', 'd7': 'bpawn', 'd8': 'bqueen',
'e1': 'wking', 'e2': 'wpawn', 'e7': 'bpawn', 'e8': 'bking',
'f1': 'wbishop', 'f2': 'wpawn', 'f7': 'bpawn', 'f8': 'bbishop',
'g1': 'wknight', 'g2': 'wpawn', 'g7': 'bpawn', 'g8': 'bknight',
'h1': 'wrook', 'h2': 'wpawn', 'h7': 'bpawn', 'h8': 'brook',
}
board2 = {'a9': 'rrook'}

board3 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

board_letter_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
]

piece_list = [
    'wpawn', 'bpawn', 'wrook', 'brook', 'wknight', 'bknight', 'wbiship', 'bbishiop', 'wqueen', 'bqueen', 'wking', 'bking'
]

def check_board_letter(lst, n):
    for each in lst:
        if isinstance(each, list):
            check_board_letter(each, n)
        if any(n in each_letter for each_letter in each):
            return True
    else:
        return False




def is_valid_chess_board(board):
    for k, v in board.items():
        if any(item == v for item in piece_list):
            return True
        else:
            return False

        for k, v in board.keys():

            if int(v) >= 9:
                return False
            if check_board_letter(board_letter_list, k) == False:
                return False
            else:
                return True

    
        


print(is_valid_chess_board(board1), "this item is supposed to be true")
print(is_valid_chess_board(board2), "This item is supposed to be False")
