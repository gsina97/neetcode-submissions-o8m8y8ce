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
        
        nodeMap = {None:None}

        curr = head

        while curr:
            node = Node(curr.val)
            nodeMap[curr] = node
            curr = curr.next

        
        curr = head

        while curr:
            node = nodeMap[curr]
            node.next = nodeMap[curr.next]
            node.random = nodeMap[curr.random]
            curr = curr.next
        
        return nodeMap[head]