from collections import defaultdict
import heapq

# COMPLETED IN 30 MINUTES ON MY OWN - however, I did just read the course on dijkstras, AND I used a pseudo-conceptual video (no code)
# as a guide (https://www.youtube.com/watch?v=bZkzH5x0SKU)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacencyList = defaultdict(set)
        shortestPaths = defaultdict(list[int])
        for i in range(1, n+1):
            adjacencyList[i] = set()

        for src, target, time in times:
            adjacencyList[src].add((time, target))

        minHeap = [(0, k)]
        shortestPaths[k] = [0, None]

        visited = set()

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)

            if node1 in visited:
                continue

            visited.add(node1)
            
            for time2, node2 in adjacencyList[node1]:

                if (node2 not in shortestPaths) or (time1 + time2 < shortestPaths[node2][0]):
                    shortestPaths[node2] = [time1 + time2, node1]
    
                heapq.heappush(minHeap, (time1 + time2, node2))

        maxTime = 0
        for i in range(1, n+1):
            # Can't reach a node
            if i not in shortestPaths:
                return -1
            maxTime = max(maxTime, shortestPaths[i][0])

        return maxTime

