# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return [True, 0]

        res = [False, 0]
        left_subtree = self.dfs(root.left)
        right_subtree = self.dfs(root.right)
        res[0] = left_subtree[0] and right_subtree[0] and (abs(left_subtree[1] - right_subtree[1]) <= 1)
        res[1] = 1 + max(left_subtree[1], right_subtree[1])

        return res



        
        