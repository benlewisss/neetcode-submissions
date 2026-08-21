class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def deep_copy_dfs(node_input, visited) -> Optional['Node']:
            # Base case: if we've reached a None neighbor (e.g. a node with
            # no more connections), there's nothing to clone.
            if not node_input:
                return None

            # If we've already cloned this node before, return the existing
            # clone instead of creating a new one. This is what prevents
            # infinite recursion when the graph has cycles, and ensures
            # each original node maps to exactly one cloned node.
            if node_input in visited:
                return visited[node_input]

            # Clone the current node (copy its value, neighbors start empty).
            cloned = Node(node_input.val)

            # Register the clone in `visited` BEFORE recursing into neighbors.
            # This is the critical step for handling cycles: if a neighbor's
            # DFS eventually leads back to `node_input`, that recursive call
            # will find it already in `visited` and stop instead of looping
            # forever.
            visited[node_input] = cloned

            # Recursively clone each neighbor, then attach the clone to our
            # new node. Because of the `visited` check above, each neighbor
            # is only actually cloned once, no matter how many times it's
            # reachable in the graph.
            for neighbor in node_input.neighbors:
                cloned.neighbors.append(deep_copy_dfs(neighbor, visited))

            # Return the fully-connected clone of this node up to the caller
            # (either the original call or a parent node's neighbor loop).
            return cloned

        # `visited` maps original_node -> cloned_node across the whole DFS,
        # so it's created once here and threaded through every recursive call.
        clone = deep_copy_dfs(node, dict())
        return clone