class Node:

    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map key to node
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    
    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if self.capacity < len(self.cache):
            # remove from list and cache
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            


        
