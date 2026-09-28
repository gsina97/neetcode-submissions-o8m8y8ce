class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        curr = []

        def dfs(i,currs):
            if target == currs:
                res.append(curr[:])
                return
            if i == len(candidates) or currs > target:
                return
            

            curr.append(candidates[i])
            dfs(i +1 , currs + candidates[i])

            curr.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, currs)
        
        dfs(0, 0)
        return res