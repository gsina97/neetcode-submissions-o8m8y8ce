class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr = []
        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append(curr[:])
                return
            

            if openN < n:
                curr.append("(")
                dfs(openN + 1, closeN)
                curr.pop()
            
            if closeN < openN:
                curr.append(")")
                dfs(openN, closeN + 1)
                curr.pop()
            
        dfs(0,0)
        resS = []
        for tmp in res:
            resS.append("".join(tmp))
        
        return resS