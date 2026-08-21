class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for node in range(n):
            graph[node] = []
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visted = set()
        components = 0

        def dfs(node):
            if node in visted:
                return False
            visted.add(node)
            for edge in graph[node]:
                dfs(edge)
            return True 
        
        for node in range(n):
            if dfs(node):
                components+=1
        
        return components
        

        


            
