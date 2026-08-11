# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        i, j, k = head, head.next, head.next.next
        i.next = None

        while j is not None:
            j.next = i
            i = j
            j = k
            if k:
                k = k.next
            else:
                k = None

        return i


        



# i     j     k 
#       i     j     k 
#             i     j     k 
#                   i     j     k  
#                         i     j     k    
#                               i     j             
# 0 <-- 1 <-- 2 <-- 3 <-- 4 <-- 5     None