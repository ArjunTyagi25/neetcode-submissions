"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        levels = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) != 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            levels.append(level) 
        
        for level in levels:
            for i in range(len(level) - 1):
                level[i].next = level[i+1]

        return root

        