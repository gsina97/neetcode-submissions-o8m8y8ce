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

        k -= 1
        dfs(root)
        print(self.heap)
        
        while k > 0:
            k -= 1
            heapq.heappop(self.heap)
        
        return self.heap[0]

