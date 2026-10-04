# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_vals = []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            self.inorder_vals.append(node.val)
            inorder(node.right)

            return
        
        inorder(root)
        self.i = 0

    def next(self) -> int:
        val = self.inorder_vals[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        if self.i < len(self.inorder_vals):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()