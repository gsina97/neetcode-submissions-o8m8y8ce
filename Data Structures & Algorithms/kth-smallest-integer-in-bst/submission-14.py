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
            

            left = dfs(node.left)
            heapq.heappush(self.heap, node.val)
            right = dfs(node.right)

            return

        dfs(root)
        while k != 1:
            heapq.heappop(self.heap)
            k -= 1
        
        return self.heap[0]