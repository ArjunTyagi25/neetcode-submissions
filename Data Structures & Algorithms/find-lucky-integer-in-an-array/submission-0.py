class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = 1 + freq.get(num, 0)

        res = -1
        for k, v in freq.items():
            if k == v:
                res = max(res, v)

        return res
        