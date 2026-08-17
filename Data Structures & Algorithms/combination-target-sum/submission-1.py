class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_subsets = []
        curr_subset = []

        def backtracking(decision_index: int):
            curr_sum = sum(curr_subset)

            if curr_sum == target:
                all_subsets.append(curr_subset.copy())
                return

            elif curr_sum > target or decision_index >= len(nums):
                return
                
            curr_subset.append(nums[decision_index])
            backtracking(decision_index)
            
            curr_subset.pop()
            backtracking(decision_index + 1)
            

        backtracking(0)
        return all_subsets