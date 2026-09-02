class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = {i : [] for i in range(n)}
        for s,d in edges:
            adj_list[s].append(d)
            adj_list[d].append(s)

        visited = set()
        def dfs(child, parent):
            if child in visited:
                return False

            visited.add(child)
            for neighbour in adj_list[child]:
                if neighbour != parent:
                    if not dfs(neighbour, child):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n
        