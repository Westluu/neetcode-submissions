class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = {}
        res = []
        for course in range(numCourses):
            course_graph[course] = []

        for src, dst in prerequisites:
            course_graph[src].append(dst)
        
        visting = set()
        visted = set()

        def checkCycle(course):
            #Prereqs pointing at each other there is a cycle
            if course in visting:
                return True
            
            #We already saw it and saw it has no cycles
            if course in visted:
                return False
            
            visting.add(course)
            for prereq in course_graph[course]:
                if checkCycle(prereq):
                    return True
            
            visting.remove(course)
            visted.add(course)
            res.append(course)

            return False
        
        for course in range(numCourses):
            if checkCycle(course):
                return []
        
        return res
            