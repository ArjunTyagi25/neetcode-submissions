class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i : [] for i in range(numCourses)} # Maps all prereq to each course so key is course and value is list of prereq
        for prereq, course in prerequisites:
            adjList[course].append(prereq)


        def dfs(course):
            if adjList[course] == []:
                return set()

            res = set()
            for prereq in adjList[course]:
                res.add(prereq)
                if prereq in course_to_all_prereqs:
                    res = res | course_to_all_prereqs[prereq]
                else:
                    course_to_all_prereqs[prereq] = dfs(prereq)
                    res = res | course_to_all_prereqs[prereq]

            return res
        
        course_to_all_prereqs = {}
        for i in range(numCourses):
            course_to_all_prereqs[i] = dfs(i)

        res = []
        for prereq, course in queries:
            if prereq in course_to_all_prereqs[course]:
                res.append(True)
            else:
                res.append(False)

        return res