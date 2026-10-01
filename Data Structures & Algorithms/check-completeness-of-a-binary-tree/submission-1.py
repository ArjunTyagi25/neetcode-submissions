# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        isNone = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if isNone:
                        return False
                    else:
                        q.append(node.left)
                        q.append(node.right)
                else:
                    isNone = True

        return True

            
        