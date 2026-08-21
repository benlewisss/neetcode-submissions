class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        queue = deque()

        neighbour_offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Find rotten fruit and total number of fruit
        fruit_count = 0
        rotten_count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    fruit_count += 1
                if grid[row][col] == 2:
                    fruit_count += 1
                    rotten_count += 1
                    queue.append((row, col))

        if fruit_count <= 0:
            return 0
        if rotten_count <= 0:
            return -1

        print(f"Starting Queue (Rotten Locations: {queue}")
        print(f"Total Num Fruit: {fruit_count}\n")

        minute = 0
        while queue:
            print(f"Minute: {minute}")
            print(f"Queue: {queue}")
            print(f"Rotten Count: {rotten_count}")

            # Goal - all fruit are rotten
            if (rotten_count >= fruit_count):
                return minute
            minute += 1

            for i in range(len(queue)):
                cell = queue.popleft()
                cell_row, cell_col = cell

                
                print(f"Cell: {cell}, Val: {grid[cell_row][cell_col]}")

                for row_offset, col_offset in neighbour_offsets:
                    neighbour = (cell_row + row_offset, cell_col + col_offset)
                    neighbour_row, neighbour_col = neighbour

                    
                    
                    # Neighbour out of bounds
                    if (neighbour_row < 0 or neighbour_row >= num_rows 
                    or neighbour_col < 0 or neighbour_col >= num_cols):
                        continue

                    # Neighbour already rotten or neighbour not a banana
                    if (grid[neighbour_row][neighbour_col] != 1):
                        continue
                    
                    # Neighbour is fresh banana, so add to queue and make rotten
                    print(f"Rotted neighbour: {neighbour}\n")
                    queue.append(neighbour)
                    grid[neighbour_row][neighbour_col] = 2
                    rotten_count += 1

        # Could not make all fruit rotten
        return -1
        
            



