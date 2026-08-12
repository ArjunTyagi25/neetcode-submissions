# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head_1, head_2 = l1, l2

        while l1 and l2:
            s = l1.val + l2.val + carry
            if s >= 10:
                s = s - 10
                carry = 1
            else:
                carry = 0
            l1.val = s
            l2.val = s

            l1 = l1.next
            l2 = l2.next

        # l2 is finished but l1 is not
        if l1 and not l2:
            while l1:
                s = l1.val + carry
                if (s >= 10):
                    s = s - 10
                    carry = 1
                else:
                    carry = 0
                l1.val = s
                
                l1 = l1.next

            if carry == 1:
                curr = head_1
                while curr.next:
                    curr = curr.next

                curr.next = ListNode(carry, None)
        
            return head_1
        # l1 is finished but l2 is not
        elif not l1 and l2:
            while l2:
                s = l2.val + carry
                if s >= 10:
                    s = s - 10
                    carry = 1
                else:
                    carry = 0
                l2.val = s

                l2 = l2.next

            if carry == 1:
                curr = head_2
                while curr.next:
                    curr = curr.next

                curr.next = ListNode(carry, None)
        
            return head_2   
        else:
            if carry == 1:
                curr = head_1
                while curr.next:
                    curr = curr.next

                curr.next = ListNode(carry, None)
        
            return head_1