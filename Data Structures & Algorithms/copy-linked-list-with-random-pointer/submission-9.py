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
        
        mapping = {None:None}

        curr = head

        while curr:
            node = Node(curr.val)
            mapping[curr] = node
            curr = curr.next

        curr = head
        while curr:
            newNode = mapping[curr]
            newNode.next = mapping[curr.next]
            newNode.random = mapping[curr.random]
            curr = curr.next

        return mapping[head]    