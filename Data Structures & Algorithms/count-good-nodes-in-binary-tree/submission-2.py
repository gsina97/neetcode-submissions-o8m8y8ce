# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node, currmax
        self.result = 0
        curr = root
        def dfs(node, currmax):
            if not node:
                return 
            
            if node.val >= currmax:
                self.result += 1
                currmax = node.val

            dfs(node.left, currmax)
            dfs(node.right, currmax)
        
        dfs(curr, curr.val)
        return self.result