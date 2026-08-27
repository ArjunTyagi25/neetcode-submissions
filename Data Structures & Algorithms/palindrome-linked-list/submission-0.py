# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        curr = head

        while curr:
            array.append(curr.val)
            curr = curr.next

        i, j = 0, len(array) - 1
        while i <= j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1

        return True


        