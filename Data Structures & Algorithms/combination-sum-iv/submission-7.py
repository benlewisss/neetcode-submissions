class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # Sort for fail early recursion
        nums.sort()
        
        dp = {}
        def recursion(curr_sum: int):
            if curr_sum > target:
                return 0
                
            if curr_sum == target:
                return 1

            if curr_sum in dp:
                return dp[curr_sum]
            
            num_valid_combinations = 0
            for i in range(len(nums)):
                num_valid_combinations += recursion(curr_sum + nums[i])

            dp[curr_sum] = num_valid_combinations
            return num_valid_combinations

        return recursion(0)