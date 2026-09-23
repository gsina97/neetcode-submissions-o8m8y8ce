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
        # old to copy

        m = {None:None}

        curr = head

        while curr:
            node = Node(curr.val)
            m[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            newNode = m[curr]
            newNode.next = m[curr.next]
            newNode.random = m[curr.random]
            curr = curr.next
        
        return m[head]
        