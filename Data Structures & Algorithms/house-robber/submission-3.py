from functools import cache

# USED HINT 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_sum = 0

        @cache
        def backtracking(house_num: int, curr_sum: int):
            nonlocal max_sum
            
            if curr_sum > max_sum:
                #print(f"Max_sum update: {max_sum} -> {curr_sum}")
                max_sum = curr_sum
            
            if house_num >= len(nums):
                #print("End of decision tree")
                return
            
            #print(f"House: {house_num} (Val={nums[house_num]}), Curr_sum: {curr_sum}, Max_sum: {max_sum}")
            backtracking(house_num + 2, curr_sum + nums[house_num])
            backtracking(house_num + 1, curr_sum)

        backtracking(0, 0)
        return max_sum
            