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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = DSU(n)

        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]

            if not uf.union(a-1,b-1):
                return [a,b] 
        