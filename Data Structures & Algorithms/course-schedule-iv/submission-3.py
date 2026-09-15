class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = { i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        # [a,b] means a is a prerequisite of course b so a → b meaning doing a unlocks b as next course
        for a, b in prerequisites:
            adj_list[a].append(b)
            inDegree[b] += 1

        q = deque()
        visited = set()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        all_prerequisites = {i : set() for i in range(numCourses)}
        while q:
            curr_course = q.popleft() # a course we can do currently

            for next_Course in adj_list[curr_course]:
                all_prerequisites[next_Course].add(curr_course)
                
                all_prerequisites[next_Course].update(all_prerequisites[curr_course])

                inDegree[next_Course] -= 1
                if inDegree[next_Course] == 0:
                    q.append(next_Course)

        res = []
        for u, v in queries:
            if u in all_prerequisites[v]:
                res.append(True)
            else:
                res.append(False)

        return res

        