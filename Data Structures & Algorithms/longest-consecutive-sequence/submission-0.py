from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0

        nums = set(nums)
        for num in nums:
            # if num - 1 not in in nums then this means this has potential to be first num in sequence
            if num - 1 not in nums:
                curr_sequence_length = 1
                while (num + curr_sequence_length) in nums:
                    curr_sequence_length += 1
                max_sequence = max(max_sequence, curr_sequence_length)
        
        return max_sequence