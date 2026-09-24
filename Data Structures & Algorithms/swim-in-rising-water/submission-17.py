from collections import defaultdict
import heapq

# I got 99.999999% of the way there on my own. I used a shitty hint which didn't actually help me it, it just pointed me into my cost
# function which I tinkered with and now it works.

# Before I changed it was this:
# new_weight = max(0, grid[new_cell[0]][new_cell[1]] - grid[cell[0]][cell[1]])

# if (new_cell not in shortestPath) or (weight1 + new_weight < shortestPath[new_cell][0]):
#     shortestPath[new_cell] = [weight1 + new_weight, cell]

# heapq.heappush(minHeap, (weight1 + new_weight, new_cell))

# Essentially, the issue was that:
# new_weight = max(0, grid[new_cell[0]][new_cell[1]] - grid[cell[0]][cell[1]])
# should have been
# new_weight = max(0, grid[new_cell[0]][new_cell[1]] - weight1)

# We were only considering the weighted difference between the two squares rather than the rolling weight difference.



class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        shortestPath = defaultdict(list)
        visited = set()

        # Heap val: (weight, (row, col))
        minHeap = [(grid[0][0], (0, 0))]
        shortestPath[(0, 0)] = [grid[0][0], None]

        while minHeap:
            weight1, cell = heapq.heappop(minHeap)

            if cell in visited:
                continue

            visited.add(cell)

            traversal_directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
            for direction in traversal_directions:
                new_cell = (cell[0] + direction[0], cell[1] + direction[1])

                if (new_cell[0] < 0 or new_cell[0] >= num_rows or new_cell[1] < 0 or new_cell[1] >= num_cols):
                    continue
                
                if new_cell in visited:
                    continue

                # The weight for the new cell is the difference in elevation between current cell and this cell.
                new_weight = max(weight1, grid[new_cell[0]][new_cell[1]])

                if (new_cell not in shortestPath) or (new_weight < shortestPath[new_cell][0]):
                    shortestPath[new_cell] = [new_weight, cell]
                
                heapq.heappush(minHeap, (new_weight, new_cell))

        return shortestPath[(num_rows - 1, num_cols - 1)][0]