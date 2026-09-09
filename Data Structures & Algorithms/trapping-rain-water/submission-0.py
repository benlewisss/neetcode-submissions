# Used Hint 1 + Hint 2
class Solution:
    def trap(self, height: List[int]) -> int:

        # Plan:
        # Start Left and Right pointer, move right pointer until you reach a height greater than 
        # the left pointer, calculate the water level between the two pointers and add it to the total,
        # then move the left pointer to the right one and remove the heights encountered from the water level total.
        # Be sure to do this left pointer subtraction in isolation with that iteration, we should cap the total for any iteration 
        # at a minimum of 0 so we don't remove from the running total.
        # Once R is out of bounds, we reverse the process, working our way back from the right to find any pools.
        

        width = len(height)
        water_levels = list()

        L = 0
        R = 1

        total_water = 0

        # Work from the left
        while R < width:
            left_height = height[L]
            right_height = height[R]

            if (right_height >= left_height):
                L += 1
                current_bucket = min(left_height, right_height) * (R - L)

                while L < R:
                    current_bucket -= height[L]
                    L += 1

                current_bucket = max(current_bucket,  0)
                total_water += current_bucket

            R += 1


        R -= 1
        highest_point = L
        L = R - 1

        # Work from the right
        while L >= highest_point:
            left_height = height[L]
            right_height = height[R]

            if (left_height >= right_height):
                R -= 1
                current_bucket = min(left_height, right_height) * (R - L)

                while R > L:
                    current_bucket -= height[R]
                    R -= 1

                current_bucket = max(current_bucket,  0)
                total_water += current_bucket

            L -= 1

        return total_water

        