class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        len_nums = len(nums)
        complements = dict()
        for i in range(len_nums):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            
            complement = target - nums[i]
            complements[complement] = i