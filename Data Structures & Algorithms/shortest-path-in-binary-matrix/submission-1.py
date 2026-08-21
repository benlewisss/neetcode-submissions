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

        

        # While something still in the queue
        while queue:
            length += 1
            len_queue = len(queue)
        
            for i in range(len_queue):

                cell = queue.popleft()

                if cell == (num_rows-1, num_cols-1):
                    return length

                for ro, co in neighbours:
                    row = cell[0] + ro
                    col = cell[1] + co

                    neighbour = (row, col)

                    if (neighbour in visited):
                        continue

                    if (row < 0 or row >= num_rows or col < 0 or col >= num_cols):
                        continue
                    
                    if (grid[row][col] != 0):
                        continue

                    queue.append(neighbour)
                    visited.add(neighbour)

        return -1