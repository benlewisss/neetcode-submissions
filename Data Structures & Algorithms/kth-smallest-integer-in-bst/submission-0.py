# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import itertools

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Generator for retrieving sorted values
        def retrieveSmallest(root: TreeNode) -> Generator[int]:
            if root is None:
                return root
            
            yield from retrieveSmallest(root.left)
            yield root.val
            yield from retrieveSmallest(root.right)

        for index, num in enumerate(retrieveSmallest(root)):
            if (index+1 == k):
                return num