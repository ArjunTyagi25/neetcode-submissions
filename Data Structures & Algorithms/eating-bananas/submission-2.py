class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        min_k = float('inf')

        while L<=R:
            M = (L+R)//2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/M)
            
            if hours > h:
                L = M + 1
            else:
                min_k = min(min_k, M)
                R = M - 1
        
        return min_k