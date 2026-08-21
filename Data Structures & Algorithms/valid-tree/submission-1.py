class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #input: N nodes along with a list of edges of an undirected graph
        #output: If given N and edges determine if the undirected graph of these is a valid tree

        #By definition a valid consist of a graph such that its fully connected meaning that every
        #node can reach every other node and there is no cycles that exist

        #How can we check if this is fully connected
            #we can run BFS/DFS on a node and see if we can touch all n-1 nodes
        
        #How can we check if no cycle exist
            #we can use DFS/BFS while keeping a visted set
            #if we encounter a visted node then there is a cycle that exist
        
        #Putting it together, 
        #we first construct the graph
        #then we can use DFS
        #while running this DFS we keep track of a visited set
        #if we encounter a node in the visted we return (as its a cycle and no longer a valid tree)

        #then we check the len of visted, if the len is == n, then every node is connected
        #as we traverse to all nodes from one node, thus making the tree valid
        #returning true
        #otherwise return false

        #create the graph
        graph = {}
        for node in range(n):
            graph[node] = []

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visted = set()
        def dfs(node, parent):
            #check if this is a cycle
            if node in visted:
                return False

            visted.add(node)
            for edge in graph[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            return True
        
        valid = dfs(0, -1)
        if len(visted) == n and valid:
            return True
        return False





