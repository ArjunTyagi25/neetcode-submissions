"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        new_nodes = []
        old_nodes = []

        curr = head
        while curr:
            new_node = Node(curr.val)
            new_nodes.append(new_node)
            old_nodes.append(curr)
            hash_map[curr] = new_node

            curr = curr.next

        for i in range(len(new_nodes)):
            if i != len(new_nodes)-1:
                new_nodes[i].next = new_nodes[i+1]
            else:
                new_nodes[i].next = None

            random_node = old_nodes[i].random
            if random_node is None:
                new_nodes[i].random = None
            else:
                new_nodes[i].random = hash_map[old_nodes[i].random]
                
        if len(new_nodes) != 0:
            return new_nodes[0]
        else:
            return None
        