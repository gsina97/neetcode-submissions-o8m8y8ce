class UF:
    def __init__(self,n):
        self.parent = list(range(n))

    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        self.parent[root_a] = root_b
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UF(n)

        for a,b in edges:
            uf.union(a,b)
        
        res = set()
        for i in range(n):
            res.add(uf.find(i))
        
        return len(res)


        