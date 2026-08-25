class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Logic is: The number of unique paths from any particular location is simply the number of
        # unique paths from each adjacent square summed. This is recursive, and because if we map
        # out the decision tree, many paths are replicated, we can simply cache them.

        unique_path_cache = dict()
        
        def backtracking(row: int, col: int) -> int:
            # Only bounds checking in one direction because we only move down and right
            if (row >= m or col >= n):
                return 0
            
            # Reached target, theres only 1 path from here because we're already here
            if (row == m - 1 and col == n - 1):
                return 1

            if (row, col) in unique_path_cache:
                return unique_path_cache[(row, col)]

            unique_path_cache[(row, col)] = backtracking(row + 1, col) + backtracking(row, col + 1)
            return unique_path_cache[(row, col)]

        return backtracking(0, 0)