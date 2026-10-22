class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Base case
        if grid[0][0] != 0: return -1
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Initialise data structures
        queue = deque()
        visited = set()

        # Neighbours to visit
        neighbours = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]

        # We start from the upper left cell
        queue.append((0,0))
        visited.add((0,0))

        # Length of path starts at zero of course
        length = 0

        # Process the queue level by level (BFS)
        while queue:

            # Each iteration of this outer loop = one level/one step further
            length += 1

            # Only process nodes already in the queue at the start of this level.
            # Neighbours found during this loop get added for the *next* level,
            # so we cap the range here to avoid processing them early.
            for i in range(len(queue)):

                cell = queue.popleft()

                # Reached the target
                if cell == (num_rows-1, num_cols-1):
                    return length

                # Check all neighbours of the current cell
                for ro, co in neighbours:
                    row = cell[0] + ro
                    col = cell[1] + co

                    neighbour = (row, col)

                    # Skip if already visited
                    if (neighbour in visited):
                        continue

                    # Skip if out of bounds
                    if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                        continue
                    
                    # Skip if blocked
                    if (grid[row][col] != 0):
                        continue

                    # Valid neighbour: queue it and mark visited
                    queue.append(neighbour)
                    visited.add(neighbour)

        return -1

        return -1