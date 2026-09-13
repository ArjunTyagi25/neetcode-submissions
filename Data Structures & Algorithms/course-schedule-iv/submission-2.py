class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = [[False]*numCourses for i in range(numCourses)]
        for p, c in prerequisites:
            prereq[p][c] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if prereq[i][k] and prereq[k][j]:
                        prereq[i][j] = True

        res = []
        for p, c in queries:
            res.append(prereq[p][c])

        return res