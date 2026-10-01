class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        res = []
        for num1 in nums1:
            for i in range(len(nums2)):
                if nums2[i] == num1:
                    break

            j = i
            while j < len(nums2):
                if nums2[j] > num1:
                    res.append(nums2[j])
                    break
                j += 1

            if j == len(nums2):
                res.append(-1)

        return res