from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        boundary = len(nums) // 3

        freq = defaultdict(int)
        out = set()
        for num in nums:
            freq[num] += 1
            if freq[num] > boundary:
                out.add(num)

        return list(out)