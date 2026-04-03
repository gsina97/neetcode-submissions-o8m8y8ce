class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.cache.get(key, [])

        l , r = 0 , len(values) - 1
        while r >= l:
            m = (l + r ) // 2

            if values[m][1] == timestamp:
                res = values[m][0]
                break
            elif  values[m][1] > timestamp:
                r = m - 1
            else:
                res =  values[m][0]
                l = m + 1
        return res

        
        





# need cache

# cache key - > [value, ts]