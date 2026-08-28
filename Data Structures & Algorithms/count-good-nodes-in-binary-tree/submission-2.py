# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs_preorder(node, curr_max):
            if not node:
                return curr_max

            if node.val >= curr_max:
                self.res += 1
                dfs_preorder(node.left, node.val)
                dfs_preorder(node.right, node.val)
            else:
                dfs_preorder(node.left, curr_max)
                dfs_preorder(node.right, curr_max)

        dfs_preorder(root, float('-inf'))
        return self.res
        