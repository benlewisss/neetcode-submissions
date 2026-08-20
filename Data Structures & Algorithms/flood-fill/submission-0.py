class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        target_colour = image[sr][sc]
        num_rows = len(image)
        num_cols = len(image[0])

        def dfs(image, row, col, visited):
            # Base case 1 - Out of bounds
            if (row < 0 or row >= num_rows) or (col < 0 or col >= num_cols):
                print(f"BASE OOB: Row: {row}, Col: {col}")
                return

            # Base case 2 - already visited pixel
            if (row, col) in visited:
                print(f"BASE Already visited: Row: {row}, Col: {col}")
                return

            # Base case 3 - pixel is not target pixel 
            if (image[row][col] != target_colour):
                print(f"BASE Pixel not target: Row: {row}, Col: {col}, Colour: {image[row][col]}")
                return

            visited.add((row, col))
            image[row][col] = color
            print(f"Visited: Row: {row}, Col: {col}, Val: {image[row][col]} -> {color}")
            
            dfs(image, row - 1, col, visited)
            dfs(image, row + 1, col, visited)
            dfs(image, row, col - 1, visited)
            dfs(image, row, col + 1, visited)

        dfs(image, sr, sc, set())    
        
        return image

             