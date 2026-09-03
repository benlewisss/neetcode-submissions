import copy
import pprint

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        # This is the same as the Viola-Jones integral image I learned about in uni Comp Vis
        # Because it's a 2D grid, each "prefix" in a prefix-sum table musn't just be the sum of all numbers
        # to it's left, it's the sum of all number's above and to the left of it (in 2D, not 1D).

        self.matrix = matrix
        self.summed_area_table = copy.deepcopy(matrix)


        # To populate prefix sum: for any val [i][j], sum is [i][j] + [i-1][j] + [i][j-1] - [i-1][j-1]
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for row in range(num_rows):
            for col in range(num_cols):
                north_val = (self.summed_area_table[row - 1][col] if row >= 1 else 0)
                west_val = (self.summed_area_table[row][col - 1] if col >= 1 else 0)
                north_west_val = (self.summed_area_table[row - 1][col - 1] if (row >= 1 and col >= 1) else 0)
                self.summed_area_table[row][col] = matrix[row][col] + north_val + west_val - north_west_val

        pprint.pp(self.summed_area_table)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        north_val = (self.summed_area_table[row1 - 1][col2] if row1 >= 1 else 0)
        west_val = (self.summed_area_table[row2][col1 - 1] if col1 >= 1 else 0)
        north_west_val = (self.summed_area_table[row1 - 1][col1 - 1] if (row1 >= 1 and col1 >= 1) else 0)

        return (self.summed_area_table[row2][col2] - north_val - west_val + north_west_val)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)