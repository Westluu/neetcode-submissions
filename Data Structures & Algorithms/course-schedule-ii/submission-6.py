class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            print(course)
            if course in visted:
                continue
            else:
                cycle = self.isCycle(course, courseList, visted, local_visted)
                if cycle: return []

        # Getting Order
        # create a list from courseMap by shortest pre-req
        # get min pre-req (must have no pre-req), then put into return list -> ordered
        # remove it and remove all values of that node from other nodes
        # then resort the list
        # repeat until empty

        return_list = []
        
        cl = []
        for course in courseList:
            cl.append((course, courseList[course]))
        cl = list(sorted(cl, key=lambda x: len(x[1])))
        

        while len(cl) > 0:
            min_c = cl.pop(0)
            return_list.append(min_c[0])

            for c in cl:
                if min_c[0] in c[1]:
                    c[1].remove(min_c[0])
            cl = list(sorted(cl, key=lambda x: len(x[1])))
        

         # final ending append
        for j in range(0, numCourses):
            if not j in return_list:
                return_list.append(j)

        return return_list


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