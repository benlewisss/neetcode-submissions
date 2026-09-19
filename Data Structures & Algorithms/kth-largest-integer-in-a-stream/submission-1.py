import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k = k

        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []
        for i in range(self.k-1):
            temp.append(heapq.heappop(self.heap))
        val = -self.heap[0]
        
        for num in temp:
            heapq.heappush(self.heap, num)

        return val
        
