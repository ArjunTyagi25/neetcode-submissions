# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest_element = []

        def dfs_inorder(node):
            if not node:
                return None

            dfs_inorder(node.left)
            self.k_smallest_element.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(root)

        return self.k_smallest_element[k-1]