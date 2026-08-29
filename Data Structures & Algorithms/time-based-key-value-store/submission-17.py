class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        
        vals = self.store[key]

        l = 0
        r = len(vals) - 1

        while r >= l:
            m = (l + r) // 2

            if vals[m][1] == timestamp:
                return vals[m][0]
            elif vals[m][1] > timestamp:
                r = m -1
            else:
                res = vals[m][0]
                l = m + 1
        
        return res

