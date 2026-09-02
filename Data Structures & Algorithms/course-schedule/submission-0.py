class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] is []:
                return True

            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
                else:
                    preMap[course].remove(prereq)
            visited.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
