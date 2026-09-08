from collections import Counter, defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_seen = set()
        row_seen = set()

        for i in range(9):
            for j in range(9):
                
                if (board[i][j] != '.') and (board[i][j] in row_seen):
                    return False
                else:
                    row_seen.add(board[i][j])
                
                if (board[j][i] != '.') and (board[j][i] in col_seen):
                    return False
                else:
                    col_seen.add(board[j][i])

            col_seen.clear()
            row_seen.clear()

        for row in range(0, 9, 3):
            seen = set()
            for col in range(0, 9, 3):
                row1 = board[row][col:col+3]
                row2 = board[row + 1][col:col+3] 
                row3 = board[row + 2][col:col+3]
                rows = row1 + row2 + row3
                for val in rows:
                    if (val != '.') and (val in seen):
                        return False
                    seen.add(val)
                seen.clear()


        return True