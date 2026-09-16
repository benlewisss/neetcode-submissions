# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Thinking: We have to traverse the tree until we reach a value that is between (inclusive) the values of
# p and q. This is where we begin the search, as it 

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        output = None
        def dfs(root, p, q) -> Optional[int]:
            nonlocal output
            if not root:
                return

            if (root.val >= p.val and root.val <= q.val) or (root.val >= q.val and root.val <= p.val):
                output = root
                return

            dfs(root.left, p, q)
            dfs(root.right, p, q)

        dfs(root, p, q)
        return output