# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {inorder[i] : i for i in range(len(inorder))}

        def dfs(L, R):
            if L > R:
                return None

            node = TreeNode(postorder.pop())
            index = inorderIndex[node.val]

            node.right = dfs(index+1, R)
            node.left = dfs(L, index-1)
            return node

        return dfs(0, len(inorder)-1)

