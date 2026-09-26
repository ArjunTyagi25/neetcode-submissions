class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)

        if p1 == p2:
            return False

        if self.rank[p1] <= self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append([cost, i, j])

        heapq.heapify(edges)
        minCost = 0
        num_edges = 0
        uf = DSU(n)

        while num_edges != n-1:
            cost, i, j = heapq.heappop(edges)

            if uf.union(i, j):
                minCost += cost
                num_edges += 1

        return minCost

        