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
        
        copiesMap = {None: None}

        curr = head
        while curr:
            copiesMap[curr] = Node(curr.val)
            curr = curr.next

        
        curr = head
        while curr:
            node = copiesMap[curr]
            node.next = copiesMap[curr.next]
            node.random = copiesMap[curr.random]
            curr = curr.next
        return copiesMap[head]

