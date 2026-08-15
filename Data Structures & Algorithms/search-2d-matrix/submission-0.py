class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        y_top, y_bottom = 0, len(matrix) - 1
        x_left, x_right = 0, len(matrix[0]) - 1

        x_mid = 0
        y_mid = 0

        while (y_top <= y_bottom):
            y_mid = y_top + ((y_bottom - y_top) // 2)
            if (target < matrix[y_mid][0]):
                y_bottom = y_mid - 1
            elif (target > matrix[y_mid][len(matrix[0]) - 1]):
                y_top = y_mid + 1
            else:
                break

        while (x_left <= x_right):
            x_mid = x_left + ((x_right - x_left) // 2)
            if (target < matrix[y_mid][x_mid]):
                x_right = x_mid - 1
            elif (target > matrix[y_mid][x_mid]):
                x_left = x_mid + 1
            else:
                return True
            
        return False