from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build adjacency list
        adjacencyList = defaultdict(set)
        for node, neighbour in edges:
            adjacencyList[node].add(neighbour)
            adjacencyList[neighbour].add(node)

        to_visit = {i for i in range(n)}
        have_visited = set()

        def dfs(node, prevNode: int = None):

            if node in have_visited:
                return

            have_visited.add(node)
            to_visit.discard(node)
            for neighbour in adjacencyList[node]:
                if neighbour == prevNode:
                    continue
                dfs(neighbour, node)

        numGraphs = 0
        while to_visit:
            dfs(to_visit.pop())
            numGraphs += 1

        return numGraphs


