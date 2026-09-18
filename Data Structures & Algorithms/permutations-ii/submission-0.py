class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr_permutation = []
        all_permutations = []

        nums.sort()

        def backtrack(pick, used):
            if len(curr_permutation) == len(nums):
                all_permutations.append(curr_permutation.copy())
                return

            for i in range(len(nums)):
                if pick[i]:
                    continue
                
                curr_permutation.append(nums[i])
                pick[i] = True
                used[nums[i]] = True

                backtrack(pick, used)

                curr_permutation.pop()
                pick[i] = False
                used[nums[i]] = False

        backtrack([0] * len(nums), {nums[i]: False for i in range(len(nums))})
        all_tuples = [tuple(a) for a in all_permutations]
        all_tuples = set(all_tuples)
        return [list(a) for a in all_tuples]