class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
        self.cache = {} # map key -> Node(key,val)
        
    
    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        self.right.prev = node
        node.next = self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if self.capacity < len(self.cache):
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
