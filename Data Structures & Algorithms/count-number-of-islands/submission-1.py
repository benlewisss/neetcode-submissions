class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        island_size = 0
        def dfs(grid, row, col):
            nonlocal island_size

            # Base Case 1: Water (Out of Bounds)
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                return 0

            # Base Case 2: Already Visited
            if (grid[row][col] == "2"):
                return 0

            # Base Case 3: Water (In Bounds)
            if (grid[row][col] == "0"):
                return 0

            # Indicate visited by changing 1 -> 2
            grid[row][col] = "2"
            island_size += 1
            
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                island_size = 0
                dfs(grid, row, col)
                if (island_size > 0): num_islands += 1

        return num_islands