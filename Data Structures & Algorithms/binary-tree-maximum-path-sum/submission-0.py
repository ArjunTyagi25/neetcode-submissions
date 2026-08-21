# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_subtree_maxSum = max(0, dfs(node.left))
            right_subtree_maxSum = max(0, dfs(node.right))

            self.maxSum = max(self.maxSum, left_subtree_maxSum + node.val + right_subtree_maxSum)

            return node.val + max(left_subtree_maxSum, right_subtree_maxSum)

        dfs(root)
        return self.maxSum

            


            
        