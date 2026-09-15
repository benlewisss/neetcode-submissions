# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(node, curr_depth):
            if not node:
                return curr_depth

            curr_depth += 1
            curr_depth = max(findDepth(node.left, curr_depth), findDepth(node.right, curr_depth))

            return curr_depth



        return findDepth(root, 0)