"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]

            newNode = Node(node.val)
            nodeMap[node] = newNode

            for n in node.neighbors:
                n2 = dfs(n)
                newNode.neighbors.append(n2)
            return newNode

        
        dfs(node)
        return nodeMap[node]
