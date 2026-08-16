# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return list(self.inorderTraverse(root))

    def inorderTraverse(self, root: TreeNode):
        if not root:
            return
        yield from self.inorderTraverse(root.left)
        yield root.val
        yield from self.inorderTraverse(root.right)