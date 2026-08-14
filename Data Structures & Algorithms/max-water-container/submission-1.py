class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        max_container_size = 0

        left_ptr = 0
        right_ptr = 1
        while (left_ptr < len_heights):

            # Optimisation
            if (heights[left_ptr] * (len_heights-left_ptr) < max_container_size):
                left_ptr += 1
                right_ptr = left_ptr + 1
                continue

            if (right_ptr >= len_heights):
                left_ptr += 1
                right_ptr = left_ptr + 1
                continue
            
            max_container_size = max(max_container_size, self.calculateArea(heights, left_ptr, right_ptr))
            right_ptr += 1


        return max_container_size

    def calculateArea(self, heights: List[int], bar1: int, bar2: int) -> int:
        water_height = min(heights[bar1], heights[bar2])
        return (bar2-bar1) * water_height