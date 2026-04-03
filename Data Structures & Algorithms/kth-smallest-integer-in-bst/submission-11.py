# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        
        def dfs(node):
            if not node:
                return

            heapq.heappush(self.heap, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        while k:
            k -= 1
            if not k:
                return heapq.heappop(self.heap)
            heapq.heappop(self.heap)
        