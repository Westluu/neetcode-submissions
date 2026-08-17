"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visted_copy = {}
        def dfs(node):
            if node in visted_copy:
                return visted_copy[node]
            visted_copy[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                visted_copy[node].neighbors.append(dfs(neighbor))
            return visted_copy[node]

        if node:
            return dfs(node)
    
        return None


            
            

        