class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        curr = []
        res = []

        def dfs(i, s):
            if s == target:
                res.append(curr[:])
                return
            if i == len(nums):
                return
            if target < s:
                return
            

            curr.append(nums[i])
            dfs(i, s + nums[i])
            curr.pop()
            dfs(i + 1, s)
            return
        
        dfs(0,0)
        return res