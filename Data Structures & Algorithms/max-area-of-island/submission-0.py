class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        island_size = 0
        max_island_size = 0

        def dfs(grid, row, col):
            nonlocal island_size

            # Base Case 1: Water (Out of Bounds)
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                return 0

            # Base Case 2: Water (In Bounds)
            if (grid[row][col] == 0):
                return 0

            # Indicate visited by changing 1 to 0 (water, which we already check for - implicit visited set)
            grid[row][col] = 0
            island_size += 1
            
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                island_size = 0
                dfs(grid, row, col)
                max_island_size = max(island_size, max_island_size)

        return max_island_size