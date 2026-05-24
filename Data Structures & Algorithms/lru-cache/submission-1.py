class Node:
    def __init__(self, key, val):
        self.key =key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        #map to get o(1) lookup
        self.cache = {}

        #keeping track of LRU
        #where items in front are most recent and towrds the tail least recent
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            #move that node to the front
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt

        #make current node prev and next point to each other
        prev.nxt = node.nxt
        nxt.prev = prev

        #make node pointers gone
        node.nxt = None
        node.prev = None
    
    def insert(self, node):
        head_next = self.head.nxt
        head_next.prev = node
        self.head.nxt = node
        node.prev = self.head
        node.nxt = head_next

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.capacity: 
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node

