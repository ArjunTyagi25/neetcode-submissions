# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            leftLen = dfs(node.left)
            rightLen = dfs(node.right)
            self.res = max(self.res, leftLen + rightLen)

            return 1 + max(leftLen, rightLen)

        dfs(root)
        return self.res


        