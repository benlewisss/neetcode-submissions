class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_size = 0

        left_ptr = 0
        right_ptr = len(heights) - 1
        while (left_ptr < right_ptr):
            max_size = max(max_size, min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr))

            if heights[left_ptr] <= heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        
        return max_size