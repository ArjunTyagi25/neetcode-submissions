# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            elif not node1 and node2:
                new_node = TreeNode(node2.val)
                new_node.left = dfs(node1, node2.left)
                new_node.right = dfs(node1, node2.right)

                return new_node
            elif node1 and not node2:
                new_node = TreeNode(node1.val)
                new_node.left = dfs(node1.left, node2)
                new_node.right = dfs(node1.right, node2)

                return new_node
            else:
                new_node = TreeNode(node1.val + node2.val)
                new_node.left = dfs(node1.left, node2.left)
                new_node.right = dfs(node1.right, node2.right)

                return new_node

        new_root = dfs(root1, root2)
        return new_root