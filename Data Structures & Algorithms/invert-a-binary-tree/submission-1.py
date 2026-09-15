# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Did in 5 mins
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def postorder(node):
            if not node:
                return None

            postorder(node.left)
            postorder(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp
            return node

        return postorder(root)
