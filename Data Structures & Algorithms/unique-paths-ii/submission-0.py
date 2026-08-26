class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        unique_path_cache = dict()
        
        def dfs(row: int, col: int) -> int:
            # Only bounds checking in one direction because we only move down and right
            if (row >= num_rows or col >= num_cols):
                return 0

            if (obstacleGrid[row][col] != 0):
                return 0
            
            # Reached target, theres only 1 path from here because we're already here
            if (row == num_rows - 1 and col == num_cols - 1):
                return 1

            if (row, col) in unique_path_cache:
                return unique_path_cache[(row, col)]

            unique_path_cache[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
            return unique_path_cache[(row, col)]

        return dfs(0, 0)