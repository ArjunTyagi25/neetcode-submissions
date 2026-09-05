import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg_gifts = [-g for g in gifts]
        heapq.heapify(neg_gifts)

        for i in range(k):
            val = int(math.sqrt(-heapq.heappop(neg_gifts)))
            heapq.heappush(neg_gifts, -val)

        res = 0
        for g in neg_gifts:
            res = res - g

        return res
