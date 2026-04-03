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
        
        pointMap = {None:None}

        curr = head

        while curr:
            node = Node(curr.val)
            pointMap[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            newNode = pointMap[curr]
            newNode.next = pointMap[curr.next]
            newNode.random = pointMap[curr.random]
            curr = curr.next
        
        return pointMap[head]
