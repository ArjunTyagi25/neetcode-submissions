# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            left_side = self.isSameTree(p.left, q.left)
            right_side = self.isSameTree(p.right, q.right)

            if left_side and right_side and p.val == q.val:
                return True
            else:
                return False
        