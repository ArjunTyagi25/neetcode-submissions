# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest_element = []
        self.res = 0

        def dfs_inorder(node):
            if not node:
                return None

            dfs_inorder(node.left)
            self.k_smallest_element.append(node.val)
            if len(self.k_smallest_element) == k:
                self.res = self.k_smallest_element[-1]
                return
            dfs_inorder(node.right)

        dfs_inorder(root)

        return self.res