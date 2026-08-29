class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        L = 0
        R = 0
        seen = set()

        for R in range(len(nums)):
            if (R - L > k):
                seen.remove(nums[L])
                L += 1

            if (nums[R] in seen):
                return True

            seen.add(nums[R])
        
        return False

        