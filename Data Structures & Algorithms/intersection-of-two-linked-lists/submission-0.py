# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_map = set()

        curr = headA
        while curr:
            hash_map.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in hash_map:
                return curr
            curr = curr.next

        return None

        