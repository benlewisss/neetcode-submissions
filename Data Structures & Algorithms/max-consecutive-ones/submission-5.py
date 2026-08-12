class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = 0

        for i in range(0, len(nums)):
            if (nums[i] == 1):
                consecutive += 1
            else:
                consecutive = 0
                
            max_consecutive = max(max_consecutive, consecutive)
            
        return max_consecutive