# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller_val = min(p.val, q.val)
        larger_val = max(p.val, q.val)

        def dfs(root):
            if smaller_val <= root.val <= larger_val:
                return root
            elif larger_val < root.val:
                return dfs(root.left)
            elif smaller_val > root.val:
                return dfs(root.right)

        return dfs(root)
        