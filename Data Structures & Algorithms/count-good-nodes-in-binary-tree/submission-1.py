# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        curr = root
        

        def dfs(node, currmax):
            if not node:
                return 0

            res = 1 if node.val >= currmax else 0
            currmax = max(currmax, node.val)

            res += dfs(node.left, currmax)
            res += dfs(node.right, currmax)

            return res

        return dfs(curr, curr.val)
            




        