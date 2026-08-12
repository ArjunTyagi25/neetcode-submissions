class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')

        L, R = 1, max(piles)
        while L <= R:
            k = (L+R)//2
            
            hours = 0
            for num in piles:
                hours += math.ceil(num/k)

            if hours > h:
                L = k + 1
            elif hours <= h:
                res = min(res, k)
                R = k - 1

        return res
        