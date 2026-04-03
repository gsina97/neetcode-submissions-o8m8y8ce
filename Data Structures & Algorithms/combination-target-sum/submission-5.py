class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        def dfs(i, s):
            if s == target:
                res.append(curr[:])
                return
            if s > target:
                return
            if i == len(nums):
                return
            
            curr.append(nums[i])
            s += nums[i]
            dfs(i, s)

            curr.pop()
            s -= nums[i]
            dfs(i + 1, s)
        
        dfs(0, 0)
        return res