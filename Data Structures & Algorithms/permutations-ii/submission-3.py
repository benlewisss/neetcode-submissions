class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr_permutation = []
        all_permutations = []

        nums.sort()

        def backtrack(pick):
            if len(curr_permutation) == len(nums):
                all_permutations.append(curr_permutation.copy())
                return

            for i in range(len(nums)):
                if pick[i]:
                    continue

                if i and nums[i] == nums[i - 1] and not pick[i - 1]:
                    continue
                
                curr_permutation.append(nums[i])
                pick[i] = True

                backtrack(pick)

                curr_permutation.pop()
                pick[i] = False

        backtrack([0] * len(nums))
        all_tuples = [tuple(a) for a in all_permutations]
        all_tuples = set(all_tuples)
        return [list(a) for a in all_tuples]