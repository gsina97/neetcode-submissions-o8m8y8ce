# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(n, l, r):
            if not n:
                return True
            
            if not (l < n.val < r):
                return False
            
            return isValid(n.left, l, n.val) and isValid(n.right, n.val, r)

        return isValid(root, float("-inf"), float("inf"))


