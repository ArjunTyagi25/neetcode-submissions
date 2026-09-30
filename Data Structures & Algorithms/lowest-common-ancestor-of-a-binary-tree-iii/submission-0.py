"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_to_root = []
        q_to_root = []

        curr = p
        while curr:
            p_to_root.append(curr)
            curr = curr.parent
        
        curr = q
        while curr:
            q_to_root.append(curr)
            curr = curr.parent

        p_to_root.reverse()
        q_to_root.reverse()

        for i in range(min(len(p_to_root), len(q_to_root))):
            if p_to_root[i] != q_to_root[i]:
                return p_to_root[i-1]
        
        if len(p_to_root) < len(q_to_root):
            return p
        else:
            return q