class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i : [] for i in range(1, n+1)}

        for src, dest, time in times:
            adj_list[src].append((dest, time))

        minHeap = [(0, k)]
        visited = {}
        heapq.heapify(minHeap)

        while minHeap:
            for i in range(len(minHeap)):
                curr_time, src = heapq.heappop(minHeap)

                if src in visited:
                    continue

                visited[src] = curr_time
                for dest, time in adj_list[src]:
                    if dest not in visited:
                        heapq.heappush(minHeap, (curr_time + time, dest))

        if len(visited) != n:
            return -1
        else:
            minTime = 0 
            for i in range(1, n+1):
                minTime = max(minTime, visited[i])
            return minTime
        