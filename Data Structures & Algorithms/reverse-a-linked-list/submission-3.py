# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        # h     r
        # 2 --> 3 --> None
        # None <-- 2 <-- 3

        head.next.next = head
        head.next = None

        return new_head












        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        return prev


        



# i     j     k 
#       i     j     k 
#             i     j     k 
#                   i     j     k  
#                         i     j     k    
#                               i     j             
# 0 <-- 1 <-- 2 <-- 3 <-- 4 <-- 5     None