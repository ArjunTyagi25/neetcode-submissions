class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        res = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2Set:
                res.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in nums1Set:
                res.add(nums2[i])

        return list(res)