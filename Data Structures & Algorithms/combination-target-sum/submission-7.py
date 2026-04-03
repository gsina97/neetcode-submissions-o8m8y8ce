class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        currS = []
        def dfs(i,curr):
            if curr == target:
                res.append(currS[:])
                return
            if i == len(nums):
                return
            if curr > target:
                return
            
            currS.append(nums[i])
            dfs(i, curr + nums[i])

            currS.pop()
            dfs(i + 1, curr)
        dfs(0,0)
        return res
