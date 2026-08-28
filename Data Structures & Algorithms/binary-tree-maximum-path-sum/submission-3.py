# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_path_maxSum = dfs(node.left)
            right_path_maxSum = dfs(node.right)

            self.max_sum = max(self.max_sum, max(0, left_path_maxSum) + node.val + max(0, right_path_maxSum))

            return node.val + max(0, left_path_maxSum, right_path_maxSum)

        dfs(root)
        return self.max_sum
            


            
        