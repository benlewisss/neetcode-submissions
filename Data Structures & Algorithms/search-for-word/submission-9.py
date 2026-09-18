class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        def backtracking(row, col, index, visited):
            if index == len(word):
                return True

            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return False

            if (row, col) in visited:
                return False
            
            letter = board[row][col]
            if letter != word[index]:
                return False

            visited.add((row, col))

            found = backtracking(row + 1, col, index + 1, visited) or backtracking(row - 1, col, index + 1, visited) or backtracking(row, col + 1, index + 1, visited) or backtracking(row, col - 1, index + 1, visited)

            visited.remove((row, col))

            return found

        exists = False
        for row in range(num_rows):
            for col in range(num_cols):
                if backtracking(row, col, 0, set()):
                    exists = True
                    break

        return exists