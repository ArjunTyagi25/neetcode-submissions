class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for point in points:
            dist.append(tuple((point[0]*point[0] + point[1]*point[1], point)))

        heapq.heapify(dist)
        res = []

        while len(res) != k:
            res.append(dist[0][1])
            heapq.heappop(dist)

        return res
        
