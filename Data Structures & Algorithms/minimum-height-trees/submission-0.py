class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = [[] for _ in range(n)]

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node, parent):
            farthest_node = node
            max_distance = 0

            for neighbour in adj_list[node]:
                if neighbour != parent:
                    n, dist = dfs(neighbour, node)
                    if dist + 1 > max_distance:
                        max_distance = 1 + dist
                        farthest_node = n

            return farthest_node, max_distance

        node_a, _ = dfs(0, -1)
        node_b, diameter = dfs(node_a, -1)
        centroid = []

        def find_centroid(node, parent):
            if node == node_b:
                centroid.append(node)
                return True

            for neighbour in adj_list[node]:
                if neighbour != parent:
                    if find_centroid(neighbour, node):
                        centroid.append(node)
                        return True
            return False

        find_centroid(node_a, -1)
        if len(centroid) % 2 != 0:
            return [centroid[len(centroid)//2]]
        else:
            return [centroid[len(centroid)//2], centroid[len(centroid)//2 - 1]]