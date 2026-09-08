from collections import deque, defaultdict, Counter


# I SPOILED THIS ONE AND CHEATED KIND OF WITH A HINT (Saw the word "bucket sort")
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        bucket = defaultdict(list)
        for key, val in freq.items():
            bucket[val].append(key)

        res = []
        res_count = 0

        count = len(nums)
        while (res_count < k) and (count >= 0):
            if count not in bucket:
                count -= 1
                continue
            
            for val in bucket[count]:
                res.append(val)
                res_count += 1
                if res_count >= k:
                    break
            
            count -= 1

        return res        