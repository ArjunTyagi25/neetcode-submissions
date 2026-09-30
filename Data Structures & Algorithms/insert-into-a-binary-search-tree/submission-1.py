# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def insert(node, parent, isLeftChild):
            if not node:
                if isLeftChild:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return

            if node.val < val:
                insert(node.right, node, False)
            else:
                insert(node.left, node, True)

            return

        insert(root, None, True)
        return root

        