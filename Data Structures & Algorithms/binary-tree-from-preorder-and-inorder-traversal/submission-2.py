# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hash_map = {}
        self.preorder_index = 0

        for i in range(len(inorder)):
            self.hash_map[inorder[i]] = i

        def constructSubtree(l, r):
            if l > r:
                return None

            if l == r:
                node = TreeNode(preorder[self.preorder_index])
                self.preorder_index += 1
                return node
            
            node = TreeNode(preorder[self.preorder_index])
            self.preorder_index += 1
            node.left = constructSubtree(l, self.hash_map[node.val] - 1)
            node.right = constructSubtree(self.hash_map[node.val] + 1, r)

            return node

        root = constructSubtree(0, len(inorder) - 1)

        return root


            

            

        
        