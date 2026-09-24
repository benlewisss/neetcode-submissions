from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # Build adjacency list + shortest path table
        adjacencyList = defaultdict(set)
        for i in range(n):
            adjacencyList[i] = set()

        for i, (src, dst) in enumerate(edges):
            adjacencyList[src].add((succProb[i], dst))
            adjacencyList[dst].add((succProb[i], src))

        shortestPath = defaultdict(list)
        visited = set()

        maxHeap = [(1, start_node)]
        shortestPath[start_node] = [1, None]

        while maxHeap:
            probabilty1, node1 = heapq.heappop_max(maxHeap)

            if node1 in visited:
                continue
            
            visited.add(node1)

            # Iterate over neighbours of node1
            for probability2, node2 in adjacencyList[node1]:
                if node2 in visited:
                    continue
                
                new_probability = probabilty1 * probability2
                if (node2 not in shortestPath) or (shortestPath[node2][0] < new_probability):
                    shortestPath[node2] = [new_probability, node1]

                heapq.heappush_max(maxHeap, (new_probability, node2))

        
        # Interpret result
        if end_node not in shortestPath:
            return 0
        else:
            return shortestPath[end_node][0]
