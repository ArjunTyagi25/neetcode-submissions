class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) != 1:
            stone_1 = -heapq.heappop(neg_stones)
            stone_2 = -heapq.heappop(neg_stones)

            if stone_1 < stone_2:
                heapq.heappush(neg_stones, stone_1 - stone_2)
            elif stone_1 > stone_2:
                heapq.heappush(neg_stones, stone_2 - stone_1)    
            else:
                heapq.heappush(neg_stones, 0)  

        return -neg_stones[0]

            

        