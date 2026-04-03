class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        curr = []
        def dfs(i, s):
            if s == target:
                res.append(curr[:])
                return
            if i == len(candidates) or s > target:
                return

            

            curr.append(candidates[i])
            s += candidates[i]

            dfs(i + 1, s)

            curr.pop()
            s -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, s)
        
        dfs(0,0)
        return res

