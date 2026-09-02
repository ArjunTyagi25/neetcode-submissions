class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        for s, d in edges:
            adj_list[s].append(d)
            adj_list[d].append(s)

        visited = set()
        def dfs(child, parent):
            if child in visited:
                return

            visited.add(child)
            for neighbour in adj_list[child]:
                if neighbour != parent:
                    dfs(neighbour, child)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)

        return res
