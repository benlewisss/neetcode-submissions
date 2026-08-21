"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def deep_copy_dfs(node_input, visited) -> Optional['Node']:

            if not node_input:
                return None
            
            if node_input in visited:
                return visited[node_input]
            
            cloned = Node()
            cloned.val = node_input.val
            visited[node_input] = cloned

            for neighbor in node_input.neighbors:
                cloned.neighbors.append(deep_copy_dfs(neighbor, visited))

            return cloned

        clone = deep_copy_dfs(node, dict())
        return clone