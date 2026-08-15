# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head, l2_head = l1, l2
        dummyNode = curr_1 = curr_2 = ListNode()
        dummyNode.next = l1_head
        carry = 0

        while l1 and l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            s = l1_val + l2_val + carry
            carry = s//10

            if s >= 10:
                s = s%10

            l1.val = l2.val = s

            curr_1 = l1
            curr_2 = l2

            l1 = l1.next
            l2 = l2.next


        if not l1:
            dummyNode.next = l2_head
            while l2:
                s = l2.val + carry
                carry = s//10

                if s >= 10:
                    s = s%10

                l2.val = s
                curr_2 = l2
                l2 = l2.next

            if carry == 1:
                curr_2.next = ListNode(carry, None)
        elif not l2:
            dummyNode.next = l1_head
            while l1:
                s = l1.val + carry
                carry = s//10

                if s >= 10:
                    s = s%10
                
                l1.val = s
                curr_1 = l1
                l1 = l1.next

            if carry == 1:
                curr_1.next = ListNode(carry, None)

        return dummyNode.next

            


            
           
            