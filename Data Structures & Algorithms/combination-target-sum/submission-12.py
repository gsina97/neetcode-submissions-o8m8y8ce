class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        def dfs(i, currs):
            if currs == target:
                res.append(curr[:])
                return
            if i == len(nums) or currs > target:
                return
            
            curr.append(nums[i])
            dfs(i, currs + nums[i])
            
            curr.pop()
            dfs(i + 1, currs)

        dfs(0,0)
        return res
