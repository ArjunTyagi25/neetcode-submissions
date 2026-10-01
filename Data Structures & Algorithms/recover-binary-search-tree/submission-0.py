# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        inorderVals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorderVals.append(node.val)
            inorder(node.right)

            return

        inorder(root)
        inorderVals.sort()
        i = 0

        def updateNode(node):
            nonlocal i
            if not node:
                return

            updateNode(node.left)
            node.val = inorderVals[i]
            i += 1
            updateNode(node.right)

            return

        updateNode(root)

        