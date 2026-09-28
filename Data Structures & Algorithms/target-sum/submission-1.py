class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # Cache Key = (index, remaining_target) where index is the current position in nums and remaining_target 
        # is the value required to reach the target.
        # Cache Value = number of different combinations ways an expression can be built to reach remaining_target
        # FROM the current position index (inclusive)
        cache = {}
    
        def dp(index, remaining_sum):
            if index >= len(nums):
                if remaining_sum == 0:
                    return 1
                return 0

            if (index, remaining_sum) not in cache:
                neg = dp(index + 1, remaining_sum - nums[index])
                pos = dp(index + 1, remaining_sum + nums[index])
                cache[(index, remaining_sum)] = pos + neg

            return cache[(index, remaining_sum)]
            
        return dp(0, target)

            