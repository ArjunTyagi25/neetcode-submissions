# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.setrecursionlimit(1000000000)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.runningTotal = 0

        def reverseInorder(node):
            if not node:
                return

            reverseInorder(node.right)
            node.val += self.runningTotal
            self.runningTotal = node.val
            reverseInorder(node.left)

            return

        reverseInorder(root)
        return root