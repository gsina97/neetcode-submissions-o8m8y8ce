class Node:

    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        self.left =  Node(0,0)
        self.right =  Node(0,0)

        # left -> LRU , right -> Most recent
        self.left.next = self.right
        self.right.prev = self.left

    # remove from list (from left)
    def remove(self, node):
        # the pointers before and after the node we want to remove
        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev

    # isert at right
    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = rightmost


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from list and delete the LRU from the cache (hashmap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



