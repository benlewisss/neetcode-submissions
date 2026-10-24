class Solution:

    # Solved on my own in 40 minutes
    # *kind of* got 1 hint which is that I was on the right path looking to check diagonal values

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])


        cache = [[-1] * num_cols for i in range(num_rows)]

        # Essentially what this recursion is doing is, for any given row and column, it checks what the largest possible diagonal
        # line of 1's it could form, which it assumes to be the largest possible square that can be formed - and then, because of the way
        # recursion works, we perform a check at each iteration STARTING from the bottom right of the diagonal line (i.e. smallest square)
        # and work out way BACK up to the calling coordinates. At each iteration, we check the horizontal squares down and vertical squares
        # right n spaces, where n is the current height of diagnonal line, if they are all 1's, then this small sub-square must be valid,
        # if this square is valid, we pass this size of the small square up the call chain, and then repeat, just by checking down and right,
        # we only need to check down and right because we've already proved that the smaller sub-square is valid. If the smaller sub-square 
        # was NOT valid, it would just return 1 (just the cell we're looking at), and the size of this square is implicitly capped to this size
        # + 1.

        max_value = 0

        def dfs(row, col):
            nonlocal max_value
            # Base cases
            # 1. Out of bounds
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                return 0

            # 2. Is a 0
            if matrix[row][col] == "0":
                return 0


            # check cache
            if cache[row][col] != -1:
                return cache[row][col]
            
            # maximum square from this location is 1 + the number of ones diagonally down to the right where it is still valid square
            # Check diagonally (max_diagonal is the longest diagonal line which exists within a valid square)
            max_diagonal = 1 + dfs(row + 1, col + 1)

            #print(f"({row}, {col}) - max_diag: {max_diagonal}")
    
            square_valid = True
            for i in range(1, max_diagonal):
                #print(f"Checking: matrix[{row + i}][{col}] = {matrix[row + i][col]}")
                #print(f"Checking: matrix[{row}][{col + i}] = {matrix[row][col + i]}")
                if (matrix[row + i][col] == "0") or (matrix[row][col + i] == "0"):
                    square_valid = False
                    break
                    
            if square_valid:
                max_value = max(max_value, max_diagonal)
                cache[row][col] = max_diagonal
                return max_diagonal

            # If our calculated max_diagonal is invalid, we are still on a single 1 anyways
            return 1

        for row in range(num_rows):
            for col in range(num_cols):
                dfs(row, col)

        #print(dfs(0, 0))
        #print(cache)
        return max_value ** 2