# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]

            res = [False, 0]

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            if left_res[0] and right_res[0] and abs(left_res[1] - right_res[1]) <= 1:
                res[0] = True

            res[1] = 1 + max(left_res[1], right_res[1])

            return res
    

        return dfs(root)[0]
        