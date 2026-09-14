"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new_node = {}

        def dfs(node):
            new_node = Node(node.val)
            old_to_new_node[node] = new_node

            for neighbor in node.neighbors:
                if neighbor not in old_to_new_node:
                    dfs(neighbor)

        dfs(node)
        for old_node, new_node in old_to_new_node.items():
            for old_neighbor in old_node.neighbors:
                new_node.neighbors.append(old_to_new_node[old_neighbor])

        return old_to_new_node[node]     