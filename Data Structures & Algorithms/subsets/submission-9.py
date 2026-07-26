class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        curr = []
        res = []


        def dfs(idx):
            if idx == len(nums):
                res.append(curr[:])
                return

            
            curr.append(nums[idx])
            dfs(idx + 1)

            curr.pop()
            dfs(idx + 1)

            return
        
        dfs(0)
        return res
