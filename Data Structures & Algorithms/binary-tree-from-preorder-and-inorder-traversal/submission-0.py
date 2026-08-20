# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i

        self.preorder_index = 0

        def dfs(l, r):
            if l>r:
                return None

            node_val = preorder[self.preorder_index]
            node = TreeNode(node_val)
            self.preorder_index += 1

            node.left = dfs(l, hash_map[node_val] - 1)
            node.right = dfs(hash_map[node_val] + 1, r)

            return node

        return dfs(0, len(inorder)-1)

            

        
        