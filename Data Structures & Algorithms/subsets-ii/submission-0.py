class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i: int, nums: List[int], curr_subset: List[int], subsets: List[List[int]]):
            if i >= len(nums):
                subsets.append(curr_subset.copy())
                return

            # Include
            curr_subset.append(nums[i])
            backtrack(i + 1, nums, curr_subset, subsets)

            # Don't include
            curr_subset.pop()
            while (i + 1 < len(nums)) and (nums[i + 1] == nums[i]): 
                i += 1
            backtrack(i + 1, nums, curr_subset, subsets)

        # Have to sort nums so that we can easily skip over duplicates
        nums.sort()
        curr_subset, subsets = [], []

        backtrack(0, nums, curr_subset, subsets)
        return subsets

        
