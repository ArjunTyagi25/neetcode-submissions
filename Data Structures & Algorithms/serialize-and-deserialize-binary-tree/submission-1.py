# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder_dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)
        return ",".join(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.i = 0

        def preorder_dfs():
            if nodes[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = preorder_dfs()
            node.right = preorder_dfs()

            return node

        return preorder_dfs()



