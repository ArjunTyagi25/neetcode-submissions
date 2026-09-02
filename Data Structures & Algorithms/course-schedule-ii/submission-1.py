class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        courses_taken = set()
        current_path = set()
        def dfs(crs):
            if crs in current_path:
                return False
            if crs in courses_taken:
                return True
            if preMap[crs] == []:
                self.res.append(crs)
                courses_taken.add(crs)
                return True

            current_path.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            current_path.remove(crs)
            self.res.append(crs)
            courses_taken.add(crs)
            preMap[crs] = []

            return True

        self.res = []
        for i in range(numCourses):
            if not dfs(i):
                return []

        return self.res