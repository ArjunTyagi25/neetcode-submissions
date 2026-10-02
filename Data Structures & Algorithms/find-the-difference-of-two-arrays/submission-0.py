class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        res = [set(), set()]

        for i in range(len(nums1)):
            if nums1[i] not in nums2Set and nums1[i] not in res[0]:
                res[0].add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1Set and nums2[i] not in res[1]:
                res[1].add(nums2[i])

        return [list(res[0]), list(res[1])]