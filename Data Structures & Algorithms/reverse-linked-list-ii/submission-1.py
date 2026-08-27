# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        prev, curr = dummyNode, head
        count = 0

        while curr:
            count += 1
            if count == left:
                break
            prev, curr = prev.next, curr.next

        prev_to_left = prev

        prev, curr = prev.next, curr.next
        for i in range(right - left):
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        prev_to_left.next.next = curr
        prev_to_left.next = prev

        return dummyNode.next

        