class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Maximum value that K can be is just the maximum value in piles
        high = max(piles)
        low = 1

        lowest_k = high

        while (low <= high):
            mid = low + ((high - low) // 2)
            num_hours = self.numHours(piles, mid)

            if num_hours <= h:
                high = mid - 1
                lowest_k = mid
            elif num_hours > h:
                low = mid + 1
                continue
        return lowest_k

        
    # Number of hours it would take to deplete all piles at k banans-per-hour
    def numHours(self, piles, k: int) -> int:
        res = 0
        for num in piles:
            res += (num + k - 1) // k
        
        return res
