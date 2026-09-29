class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next= self.right
        self.right.prev = self.left
    
    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        self.right.prev = node
        node.next = self.right
    
    def remove(self, node):
        right, left = node.next, node.prev

        left.next = right
        right.prev = left


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        n = self.cache[key]
        self.remove(n)
        self.insert(n)
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node =  Node(key,value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
