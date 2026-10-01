# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Order the index that each node appears at in the inorder list in a hash map
        inorderIndex = {inorder[i] : i for i in range(len(inorder))}

        def dfs(L, R):
            if L > R:
                return None

            # The last value in the postorder is the node to construct first
            node = TreeNode(postorder.pop())
            index = inorderIndex[node.val]

            # The value before the node's value in postorder is the right subtree so we construct right subtree first before left subtree
            node.right = dfs(index + 1, R)
            node.left  = dfs(L, index-1)

            return node

        return dfs(0, len(postorder)-1)