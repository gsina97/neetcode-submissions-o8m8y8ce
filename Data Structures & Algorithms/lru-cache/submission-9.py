class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        
    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost
        self.right.prev = node
        node.next = self.right
    
    def remove(self,node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
