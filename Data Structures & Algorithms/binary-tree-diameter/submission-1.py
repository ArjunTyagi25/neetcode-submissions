# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        self.res = 0

        # Returns the max height from that node
        def dfs(curr):
            if not curr:
                return 0

            left_side_length = dfs(curr.left)
            right_side_length = dfs(curr.right)
            self.res = max(self.res, left_side_length + right_side_length)
            return 1 + max(left_side_length, right_side_length)

        dfs(root)
        return self.res