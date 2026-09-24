class Solution:
    # DFS solution in 15 mins on my own, but recursion limits met
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row: int, col: int, visited: set):
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                return None
            
            if (row, col) in visited:
                return None

            if board[row][col] != 'O':
                return None

            visited.add((row, col))

            directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
            for direction in directions:
                dfs(row + direction[0], col + direction[1], visited)

            return visited

        excluded = set()
        # Iterate over all squares ON edge of board
        for row in range(num_rows):
            for col in range(num_cols):
                if (row > 0 and row < num_rows -1 and col > 0 and col < num_cols - 1):
                    continue

                if board[row][col] == 'O':
                    excluded.update(dfs(row, col, set()))

        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) not in excluded:
                    board[row][col] = 'X'
