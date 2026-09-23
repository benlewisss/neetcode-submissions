from collections import defaultdict

# Completed on my own in 40 mins (brute force solution)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numNodes = numEdges = len(edges)

        # Form adjacency list
        adjacencyList = defaultdict(set)
        for node, neighbour in edges:
            adjacencyList[node].add(neighbour)
            adjacencyList[neighbour].add(node)


        def dfs(node, adjacencyList, visited: set = set()):
            if node in visited:
                return False

            visited.add(node)

            if len(visited) >= numNodes:
                return True

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