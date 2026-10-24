class Solution:
    # Solved independently in 40 minutes.
    # Only hint: checking diagonal values was the right direction.

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Returns the area of the largest square containing only "1"s.

        For each cell, treat it as the top-left corner of a square and compute
        the largest valid side length. A square of side k at (row, col) requires:
          - a square of side k-1 at (row+1, col+1)  (the diagonal neighbor)
          - k-1 consecutive "1"s below (row, col) and to its right
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        NOT_COMPUTED = -1
        # memo[row][col] = largest square side with (row, col) as top-left corner
        memo = [[NOT_COMPUTED] * num_cols for _ in range(num_rows)]

        largest_side = 0

        def largest_square_at(row, col):
            """Largest square side length whose top-left corner is (row, col)."""
            nonlocal largest_side

            # Base case: out of bounds
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return 0

            # Base case: a "0" cannot be part of a square
            if matrix[row][col] == "0":
                return 0

            if memo[row][col] != NOT_COMPUTED:
                return memo[row][col]

            # Upper bound on the side length: this cell plus the largest square
            # starting at the diagonal neighbor (down and to the right).
            max_side_by_diagonal = 1 + largest_square_at(row + 1, col + 1)

            # Walk down the column and right along the row from this cell; stop at
            # the first "0". Only offsets that fit inside the diagonal bound are checked.
            max_side_by_edges = 1
            for offset in range(1, max_side_by_diagonal):
                if matrix[row + offset][col] == "0" or matrix[row][col + offset] == "0":
                    break
                max_side_by_edges += 1

            side = min(max_side_by_edges, max_side_by_diagonal)
            largest_side = max(largest_side, side)
            memo[row][col] = side
            return side

        # Try every cell as a potential top-left corner
        for row in range(num_rows):
            for col in range(num_cols):
                largest_square_at(row, col)

        return largest_side ** 2