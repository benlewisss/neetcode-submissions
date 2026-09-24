from collections import defaultdict
import heapq
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