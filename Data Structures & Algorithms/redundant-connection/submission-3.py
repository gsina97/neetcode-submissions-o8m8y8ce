class UF:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        
    def find(self,x ):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a,b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False
        
        self.parent[ra] = rb
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UF(len(edges))

        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        
