class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = { i : [] for i in range(numCourses)}
        inDegree = [0 for i in range(numCourses)]

        for a, b in prerequisites:
            preReq[b].append(a)
            inDegree[a] += 1

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        res = []

        while q:
            for _ in range(len(q)):
                course = q.popleft()
                res.append(course)

                for nextCourse in preReq[course]:
                    inDegree[nextCourse] -= 1
                    if inDegree[nextCourse] == 0:
                        q.append(nextCourse)


        if len(res) == numCourses:
            return res
        return []