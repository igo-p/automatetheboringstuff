from collections import Counter

def isValidChessBoard(dict):
    # Check the board size
    keysList = list(dict.keys())
    for key in keysList:
        if int(key[0]) > 8 or key[1] > 'h':
            return False
    
    # Check the amount of pieces per team
    piecesCount = numOfPieces(dict)
    maxCount = {
        'wking': 1,
        'bking': 1,
        'wqueen': 1,
        'bqueen': 1,
        'wknight': 2,
        'bknight': 2,
        'wbishop': 2,
        'bbishop': 2,
        'wrook': 2,
        'brook': 2,
        'wpawn': 8,
        'bpawn': 8
    }
    try:
        for piece in piecesCount.keys():
            if piecesCount[piece] > maxCount[piece]:
                return False
    except:
        print("check your pieces")
        return False
    return True

def numOfPieces(dict):
    res = Counter(dict.values())
    return res


chessBoard = {
    '1h': 'bking', 
    '6c': 'wqueen', 
    '2g': 'bbishop', 
    '5h': 'bqueen', 
    '3e': 'wking',
    '4a': 'wbishop'
              }

print(isValidChessBoard(chessBoard))

