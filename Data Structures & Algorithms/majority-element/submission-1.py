class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res, resCount = 0, 0
        for num, count in freq.items():
            if count > resCount:
                res = num
                resCount = count

        return res
        