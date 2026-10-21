class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
            
        target_subset_size = nums_sum // k

        cache = dict()
        def backtracking(used: list, curr_subset_size: int, num_subsets: int):
            if num_subsets > k:
                return False

            if num_subsets == k:
                return True

            used_tuple = tuple(used)
            if used_tuple in cache:
                return cache[used_tuple]

            possible = False
            for i in range(len(nums)):
                if used[i]:
                    continue

                if curr_subset_size + nums[i] < target_subset_size:
                    used[i] = True
                    possible = possible or backtracking(used, curr_subset_size + nums[i], num_subsets)
                    used[i] = False

                elif curr_subset_size + nums[i] == target_subset_size:
                    used[i] = True
                    possible = possible or backtracking(used, 0, num_subsets + 1)
                    used[i] = False

            cache[used_tuple] = possible
            return cache[used_tuple]

        return backtracking([False] * len(nums), 0, 0)
        

