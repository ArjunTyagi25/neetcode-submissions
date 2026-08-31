class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr_index = m + n - 1
        i, j = m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[curr_index] = nums1[i]
                i -= 1
            else:
                nums1[curr_index] = nums2[j]
                j -= 1
            curr_index -= 1

        if i < 0 and j >= 0:
            while curr_index >= 0:
                nums1[curr_index] = nums2[j]
                curr_index, j = curr_index - 1, j - 1
        
        