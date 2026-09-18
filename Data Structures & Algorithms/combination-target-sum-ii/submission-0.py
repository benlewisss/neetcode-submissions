class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        all_combinations = []
        curr_combination = []

        candidates.sort()

        def backtrack(index, curr_sum):
            if curr_sum == target:
                all_combinations.append(curr_combination.copy())
                return
            
            if curr_sum > target or index >= len(candidates):
                return

            curr_combination.append(candidates[index])
            backtrack(index + 1, curr_sum + candidates[index])

            while (index < len(candidates) - 1) and (candidates[index + 1] == candidates[index]):
                index += 1

            curr_combination.pop()
            backtrack(index + 1, curr_sum)

        backtrack(0, 0)
        return all_combinations
                
