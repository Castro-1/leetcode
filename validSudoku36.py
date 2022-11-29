def isValidSudoku(board):
    mat = {}
    cols = {}
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in row:
                    return False
                row += [board[i][j]]
                if j in cols:
                    if board[i][j] in cols[j]:
                        return False
                else:
                    cols[j] = [board[i][j]]
                cols[j] += [board[i][j]]
    for i in range(9):
        num = 0
        for j in range(9):
            if board[i][j] != ".":
                if num in mat:
                    if board[i][j] in mat[num]:
                        return False
                    mat[num] += [board[i][j]]
                else:
                    mat[num] = [board[i][j]]
            if (j+1) % 3 == 0:
                num += 1
        if (i+1) % 3 == 0:
            mat = {}
    return True


board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]
print(isValidSudoku(board))
