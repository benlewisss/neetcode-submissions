class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_permutation = []
        all_permutations = []

        def backtrack(index, used):
            if len(curr_permutation) == len(nums):
                all_permutations.append(curr_permutation.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                curr_permutation.append(nums[i])
                used[i] = True

                backtrack(index, used)

                curr_permutation.pop()
                used[i] = False


        backtrack(0, [False] * len(nums))
        return all_permutations

