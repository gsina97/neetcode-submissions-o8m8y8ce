# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValid(float("-inf"), root.val, root.left) and self.isValid(root.val, float("inf"), root.right)
        

    
    def isValid(self, mmin, mmax, n):
        if not n:
            return True
        
        if not mmin < n.val < mmax:
            return False
        
        return self.isValid(mmin, n.val, n.left) and self.isValid(n.val, mmax, n.right)