class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left


    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        node.next = self.right
        self.right.prev = node        

    def remove(self, node):
        right, left = node.next, node.prev
        left.next = right
        right.prev = left

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
        
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
