class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = 0
        for num in nums:
            freq[num] = freq[num] + 1

        output = list()

        for i in range(0, k):
            high = max(freq, key=freq.get)
            output.append(high)
            del freq[high]
        
        return output

        