class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res = []
        curr = []
        def dfs(i,currS):
            if currS == target:
                res.append(curr[:])
                return
            if i == len(candidates) or currS > target:
                return

            curr.append(candidates[i])
            dfs(i + 1, currS + candidates[i])

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            curr.pop()
            dfs(i + 1, currS)

            return
        
        dfs(0,0)
        return res
