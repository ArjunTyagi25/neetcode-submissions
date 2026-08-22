# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def postorder(node):
            if not node:
                return 0

            left_len = postorder(node.left)
            right_len = postorder(node.right)
            self.res = max(self.res, left_len + right_len)

            return 1 + max(left_len, right_len)

        postorder(root)

        return self.res


        