"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {} # Maps old nodes to new nodes

        def recursion(node):
            if not node:
                return None
            
            copy_node = Node(node.val)
            hash_map[node] = copy_node
            copy_node.neighbors = []

            for neighbor in node.neighbors:
                if neighbor in hash_map:
                    copy_node.neighbors.append(hash_map[neighbor])
                else:
                    copy_node.neighbors.append(recursion(neighbor))

            return copy_node

        return recursion(node)        