# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        dummyNode = ListNode(0, head)
        curr = dummyNode
        while curr:
            curr = curr.next
            length += 1

        node_to_remove = dummyNode
        for i in range(length-n):
            node_to_remove = node_to_remove.next

        prev_node_to_remove = dummyNode
        for i in range(length-n-1):
            prev_node_to_remove = prev_node_to_remove.next

        prev_node_to_remove.next = prev_node_to_remove.next.next

        return dummyNode.next
        