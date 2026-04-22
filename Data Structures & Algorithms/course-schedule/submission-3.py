#Plan

#Reading the pre-req list and construct a graph from it
# after construction check if a cycle exist
# if cycle return false 
# else check if len of graph > numCourses: if no return True, else return False

# how to construct graph from list (creat adjancey list)
# read pre-req list
# 



class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = {}
        visted = set()
        local_visted = set()

        #Constructing Graph
        for src, dst in prerequisites:
            if src not in courseList:
                courseList[src] = []
            if dst not in courseList:
                courseList[dst] = []
            courseList[src].append(dst)

        #Finding Cycles
        for course in courseList:
            if course in visted:
                continue
            else:
                cycle = self.isCycle(course, courseList, visted, local_visted)
                if cycle: return False
        
        
        return True


    def isCycle(self, course, courseList, visted, local_visted):
        dest = courseList[course]

        if course in local_visted:
            return True
        if course in visted:
            return False
        
        local_visted.add(course)
        visted.add(course)

        for c in dest:
            cycle = self.isCycle(c, courseList, visted, local_visted)
            if cycle: return True
        
        local_visted.remove(course)
        return False
        
        

        


        