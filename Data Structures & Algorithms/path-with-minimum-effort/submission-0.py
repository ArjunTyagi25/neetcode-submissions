class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        visited = set()
        minHeap = [(0,0,0)]
        heapq.heapify(minHeap)

        while minHeap:
            curr_max_effort, r, c = heapq.heappop(minHeap)

            if (r,c) == (ROWS-1, COLS-1):
                return curr_max_effort

            if (r,c) in visited:
                continue

            visited.add((r,c))
            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                if r+dr not in range(ROWS) or c+dc not in range(COLS) or (r+dr, c+dc) in visited:
                    continue

                heapq.heappush(minHeap, (max(curr_max_effort, abs(heights[r][c] - heights[r+dr][c+dc]))   ,r+dr, c+dc))

                    

        