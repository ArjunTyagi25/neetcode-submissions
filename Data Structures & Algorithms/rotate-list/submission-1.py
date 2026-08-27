# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummyNode = ListNode()
        dummyNode.next = head
        length = 0
        end_point, curr = dummyNode, head
        while curr:
            length += 1
            end_point = end_point.next
            curr = curr.next

        k = k % length
        if k == 0:
            return head
        break_point = head

        for i in range(length - k - 1):
            break_point = break_point.next

        new_head = break_point.next
        break_point.next = None
        end_point.next = head

        return new_head

        