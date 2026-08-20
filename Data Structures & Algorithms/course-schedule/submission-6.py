class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjancey list, check for cycle
        course_graph = {}

        for c in range(numCourses):
            course_graph[c] = []

        for src, dst in prerequisites:
            course_graph[src].append(dst)
        
        visting = set()

        #check if there is a cycle
        def checkCycle(course):
            if course in visting:
                return True
            if len(course_graph[course]) == 0:
                return False
            
            visting.add(course)
            for c in course_graph[course]:
               if checkCycle(c):
                return True
            
            visting.remove(course)
            course_graph[course] = []
            return False
        
        for c in range(numCourses):
            if checkCycle(c):
                return False
        return True
        