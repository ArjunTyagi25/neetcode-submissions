# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            if not node.left and not node.right:
                curr_sum += node.val
                if curr_sum == targetSum:
                    return True
                else:
                    return False
            else:
                curr_sum += node.val
                return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

        return dfs(root, 0)
        