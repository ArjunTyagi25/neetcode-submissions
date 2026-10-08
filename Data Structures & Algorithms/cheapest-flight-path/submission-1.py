class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = { i : [] for i in range(n)}

        for s, d, price in flights:
            adj_list[s].append((d, price))

        minHeap = [(0, src, 0)]
        heapq.heapify(minHeap)
        bestStops = {}

        while minHeap:
            totalCost, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return totalCost

            if stops > k:
                continue

            if node in bestStops and bestStops[node] < stops:
                continue
            bestStops[node] = stops

            for nextStop, price in adj_list[node]:
                heapq.heappush(minHeap, (totalCost + price, nextStop, stops + 1))

        return -1