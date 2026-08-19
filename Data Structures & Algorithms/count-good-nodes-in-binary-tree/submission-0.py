# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        max_value = float('-inf')

        def dfs(curr, max_value):
            if not curr:
                return
            
            if curr.val >= max_value:
                self.res += 1
                dfs(curr.left, curr.val)
                dfs(curr.right, curr.val)
            else:
                dfs(curr.left, max_value)
                dfs(curr.right, max_value)

            return

        dfs(root, max_value)
        return self.res
        