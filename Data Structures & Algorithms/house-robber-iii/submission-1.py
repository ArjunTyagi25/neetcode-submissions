# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def rec(node, parent_robbed):
            if not node:
                return 0

            if (node, parent_robbed) in memo:
                return memo[(node, parent_robbed)]

            if parent_robbed:
                res = rec(node.left, False) + rec(node.right, False)
            else:
                res = max(node.val + rec(node.left, True) + rec(node.right, True), rec(node.left, False) + rec(node.right, False))

            memo[(node, parent_robbed)] = res
            return res

        return rec(root, False)
            