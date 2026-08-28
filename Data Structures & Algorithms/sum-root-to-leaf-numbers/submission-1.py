# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [str(node.val)]

            left_digits = dfs(node.left)
            right_digits = dfs(node.right)

            res = []
            for num in left_digits:
                res.append(str(node.val) + num)
            
            for num in right_digits:
                res.append(str(node.val) + num)

            return res

        nums = dfs(root)
        res = 0

        for num in nums:
            res += int(num)

        return res


        