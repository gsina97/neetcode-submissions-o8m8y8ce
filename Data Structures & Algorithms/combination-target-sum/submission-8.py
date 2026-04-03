class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        def dfs(i, currsum):
            if currsum == target:
                res.append(curr[:])
                return
            if currsum > target:
                return
            if i == len(nums):
                return
            
            curr.append(nums[i])
            dfs(i, currsum + nums[i])

            curr.pop()
            dfs(i + 1, currsum)
        dfs(0,0)

        return res