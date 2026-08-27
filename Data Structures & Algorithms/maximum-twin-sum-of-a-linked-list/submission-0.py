# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the middle point
        # 2. Reverse the second half of the list
        # 3. Traverse both halves and keep track of max twin sum

        # 1. Find the middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # 2. Reverse the second half of the list
        prev, curr = None, mid
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        # 3. Traverse both halves and keep track of max twin sum
        res = float('-inf')
        list1, list2 = head, prev

        while list1 and list2:
            res = max(res, list1.val + list2.val)
            list1 = list1.next
            list2 = list2.next

        return res
        