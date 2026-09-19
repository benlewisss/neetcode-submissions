import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        # Logic is: If we have a min heap, and remove all but k elements from the top, then we are left with the k
        # largest elements in the array, and so the top of the heap will be the kth largest element.
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0] if nums else None