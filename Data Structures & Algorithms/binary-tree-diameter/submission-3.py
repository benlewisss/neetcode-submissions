# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Took 7 minutes thinking, got distracted for 10 mins with something else, then took like 45 minutes to wrap my head around this. 

# I got the following hint:
# Your intuition is spot-on: the longest path passing through any given node as the turning point is left_depth + right_depth. However, notice how dfs calculates max_distance recursively, but then discards that calculation by returning findDepth(node.left, 0) + findDepth(node.right, 0) at the end.

# I used the hint to just rewrite the dfs logic
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Maximum distance between nodes is the max depth of a left node + max depth of a right node, for every node.
    
        def findDepth(node, curr_depth):
            if not node:
                return curr_depth

            return 1 + max(findDepth(node.left, curr_depth), findDepth(node.right, curr_depth))



        def dfs(node, max_distance):
            if not node:
                return max_distance

            depth_difference = findDepth(node.left, 0) + findDepth(node.right, 0)

            return max(depth_difference, dfs(node.left, max_distance), dfs(node.right, max_distance))

        return dfs(root, 0)
    