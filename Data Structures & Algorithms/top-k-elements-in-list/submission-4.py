class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}  # maps nums to their frequency so nums: freq

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        max_freq = [(-v,k) for k,v in freq.items()]

        heapq.heapify(max_freq)

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_freq)[1])

        return res
        