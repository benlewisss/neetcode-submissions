from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Idea, do a depth first search backtrack - PICK one edge in the lists of edges to skip,
        # try traverse whole graph while skipping this edge - if it cannot be done, invalid removal
        # so choose another edge to skip and continue until you find one that can be removed.

        # It wants to remove last edge in the edges array first if there are multiple, so simply choose edges
        # to skip starting from the back of the array.

        numEdges = len(edges)

        # Form adjacency list
        adjacencyList = defaultdict(set)
        for node, neighbour in edges:
            adjacencyList[node].add(neighbour)
            adjacencyList[neighbour].add(node)


        def dfs(node, adjacencyList, visited: set = set()):
            if node in visited:
                return False

            if len(visited) >= numEdges - 1:
                return True

            visited.add(node)
            for neighbour in adjacencyList[node]:
                if dfs(neighbour, adjacencyList, visited):
                    return True

            return False


        for i in range(1, numEdges + 1):
            excludeNode, excludeNeighbour = edges[-i]

            adjacencyList[excludeNode].remove(excludeNeighbour)
            adjacencyList[excludeNeighbour].remove(excludeNode)

            if dfs(1, adjacencyList, set()):
                return edges[-i]
    
            adjacencyList[excludeNode].add(excludeNeighbour)
            adjacencyList[excludeNeighbour].add(excludeNode)

        return []