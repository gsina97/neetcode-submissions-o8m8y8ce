class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        curr = []

        def dfs(i, currS):
            if currS == target:
                res.append(curr[:])
                return
            if i == len(nums) or currS > target:
                return
            

            curr.append(nums[i])
            dfs(i,currS + nums[i])

            curr.pop()
            dfs(i + 1, currS)
            return
        
        dfs(0, 0)
        return res
            