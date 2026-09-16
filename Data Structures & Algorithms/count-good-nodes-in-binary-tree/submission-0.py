# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0

        # Pass down the largest value seen on a particular route
        def dfs(node, largest_val_seen):
            nonlocal num_good_nodes
            if not node:
                return

            print(node.val)
            if node.val >= largest_val_seen:
                num_good_nodes += 1
                largest_val_seen = node.val
            
            dfs(node.left, largest_val_seen)
            dfs(node.right, largest_val_seen)

        dfs(root, root.val)
        return num_good_nodes
