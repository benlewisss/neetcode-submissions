# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def maxDepth(node, curr_depth):
            if not node:
                return curr_depth
            
            return 1 + max(maxDepth(node.left, curr_depth), maxDepth(node.right, curr_depth))

        def dfs(node, max_difference):
            if not node:
                return max_difference
            
            left_depth = maxDepth(node.left, 0)
            right_depth = maxDepth(node.right, 0)

            return max(max_difference, abs(right_depth - left_depth), dfs(node.left, max_difference), dfs(node.right, max_difference))

        return dfs(root, 0) <= 1
