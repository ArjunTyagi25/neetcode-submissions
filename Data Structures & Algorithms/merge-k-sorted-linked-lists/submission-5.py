# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        def div_and_con(lists, l, r):
            if l>r:
                return None
            elif l==r:
                return lists[l]

            mid = (l+r)//2
            left_list = div_and_con(lists, l, mid)
            right_list = div_and_con(lists, mid+1, r)

            curr_1, curr_2 = left_list, right_list
            dummyNode = ListNode()
            curr = dummyNode
            
            while curr_1 and curr_2:
                if curr_1.val <= curr_2.val:
                    curr.next = curr_1
                    curr_1 = curr_1.next
                else:
                    curr.next = curr_2
                    curr_2 = curr_2.next
                curr = curr.next

            if curr_1:
                curr.next = curr_1
            if curr_2:
                curr.next = curr_2

            return dummyNode.next

        return div_and_con(lists, 0, len(lists) - 1)

            



        