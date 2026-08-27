# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        curr = head
        if length%2 != 0:
            for i in range(length//2):
                curr = curr.next
        else:
            for i in range(length//2):
                curr = curr.next

        return curr
        