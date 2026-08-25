class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        curr =[]

        def dfs(i, currS):
            if currS == target:
                res.append(curr[:])
                return
            if currS > target or i == len(candidates):
                return
            

            curr.append(candidates[i])
            dfs(i + 1, currS + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            dfs(i + 1, currS)
            
            return
        
        dfs(0,0)

        return res
