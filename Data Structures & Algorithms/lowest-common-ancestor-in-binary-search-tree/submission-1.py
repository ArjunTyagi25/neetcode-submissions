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

        if smaller_val <= root.val <= larger_val:
            return root
        elif root.val < smaller_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif larger_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        