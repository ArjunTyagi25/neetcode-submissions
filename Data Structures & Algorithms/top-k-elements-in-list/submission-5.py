class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, f in freq.items():
            count[f].append(num)

        res = []
        for i in range(len(count)-1, -1, -1):
            for num in count[i]:
                res.append(num)

                if len(res) == k:
                    return res
        