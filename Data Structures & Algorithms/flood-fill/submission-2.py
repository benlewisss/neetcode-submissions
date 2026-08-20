class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        target_colour = image[sr][sc]
        num_rows = len(image)
        num_cols = len(image[0])

        def dfs(image, row, col, visited):
            # Base case 1 - Out of bounds
            if (row < 0 or row >= num_rows) or (col < 0 or col >= num_cols):
                return

            # Base case 2 - already visited pixel
            if (row, col) in visited:
                return

            # Base case 3 - pixel is not target pixel 
            if (image[row][col] != target_colour):
                return

            visited.add((row, col))
            image[row][col] = color
            
            dfs(image, row - 1, col, visited)
            dfs(image, row + 1, col, visited)
            dfs(image, row, col - 1, visited)
            dfs(image, row, col + 1, visited)

        dfs(image, sr, sc, set())    
        
        return image

# TO IMPROVE:
# Your current logic is quite solid! Using a DFS with a visited set correctly prevents infinite recursion. However, consider if you truly need that extra memory for the set.

# Think about the case where the starting pixel's color is already equal to the target color. If you don't use a visited set, how would your code react to this scenario?

# In flood fill, if the new color is different from the original color, the color change itself acts as a 'visited' marker. The only edge case where you might loop forever is if image[sr][sc] == color.

             