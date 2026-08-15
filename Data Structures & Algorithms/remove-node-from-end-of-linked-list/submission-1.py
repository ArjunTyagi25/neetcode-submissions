# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummyNode = ListNode()
        dummyNode.next = head

        curr = head
        while curr:
            length += 1
            curr = curr.next

        prev = dummyNode
        for i in range(length-n):
            prev = prev.next

        prev.next = prev.next.next

        return dummyNode.next

        