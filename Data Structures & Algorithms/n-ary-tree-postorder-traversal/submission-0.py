"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs_postorder(node):
            if not node:
                return None

            for child in node.children:
                dfs_postorder(child)

            res.append(node.val)

        dfs_postorder(root)

        return res