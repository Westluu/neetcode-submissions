"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        return self.createCopyHelper(head, node_map)

    
    def createCopyHelper(self, head, node_map):
        if not head:
            return None

        if id(head) in node_map:
            return node_map[id(head)]

        copy = Node(head.val)
        node_map[id(head)] = copy
        
        copy.next = self.createCopyHelper(head.next, node_map)
        copy.random = self.createCopyHelper(head.random, node_map)
        
        return copy
        

        
        
        
