# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return None

        # 1. plit the list into two halves
        # 2. Reverse the second-half of the list
        # 3. Merge first-half and second-half alternatively

        # 1. Split the list into two halves
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        curr = head
        for i in range(int(length/2)-1):
            curr = curr.next

        first_half = head
        if length % 2 == 0:
            second_half = curr.next
            curr.next = None
        else:
            second_half = curr.next.next
            curr.next.next = None

        # 2. Reverse the second-half of the list
        prev, curr = None, second_half

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        second_half = prev

        # 3. Merge first-half and second-half alternatively
        curr_1, curr_2 = first_half, second_half

        while curr_1 and curr_2:
            temp1 = curr_1.next
            curr_1.next = curr_2
            temp2 = curr_2.next
            curr_2.next = temp1

            curr_1 = temp1
            curr_2 = temp2
        
        