# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Thinking: We have to traverse the tree until we reach a value that is between (inclusive) the values of
# p and q. This is where we begin the search, as it 

# Came up with DFS solution in 15 mins, but I know bfs would be better as it's level by level so breaks earlier.
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        output = None
        def search(root, p, q) -> Optional[int]:
            nonlocal output
            if not root:
                return

            if p.val > root.val and q.val > root.val:
                search(root.right, p, q)
            
            elif p.val < root.val and q.val < root.val:
                search(root.left, p, q)

            else:
                output = root
                return

        search(root, p, q)
        return output