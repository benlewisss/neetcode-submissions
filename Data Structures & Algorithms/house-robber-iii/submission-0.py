# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


cache = dict()

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Boolean value tracks whether the given node is able to be robbed
        def backtracking(root: TreeNode, canRob: bool) -> int:
            if not root:
                return 0

            max_val = 0

            if (root, canRob) in cache:
                return cache[(root, canRob)]

            # Choices
            # 1. Skip this house
            max_val = max(max_val, backtracking(root.left, True) + backtracking(root.right, True))
            
            # # 2. Rob this house and skip children (only possible if house is robbable, given flag)
            if canRob == True:
                max_val = max(max_val, root.val + backtracking(root.left, False) + backtracking(root.right, False))

            cache[(root, canRob)] = max_val
            return cache[(root, canRob)]

        return backtracking(root, True)