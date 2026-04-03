class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> Node      ()
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        self.right.prev = node
        node.next = self.right

    def remove(self, node):
        left, right = node.prev, node.next
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
            node = self.cache[key]
            del self.cache[key]
            self.remove(node)
        
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node

        if self.capacity < len(self.cache):
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)

        
