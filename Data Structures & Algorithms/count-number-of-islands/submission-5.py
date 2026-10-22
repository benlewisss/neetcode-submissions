class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(row, col):
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        num_islands = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands

            