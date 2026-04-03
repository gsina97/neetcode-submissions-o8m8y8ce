class TimeMap:

    def __init__(self):
        # key -> list of values 
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []

        self.cache[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        values = self.cache.get(key, [])

        l = 0
        r = len(values) - 1
        res = ""
        while r >= l:
            m = (l + r ) // 2

            if values[m][0] == timestamp:
                res = values[m][1]
                break
            elif values[m][0] > timestamp:
                r = m -1
            else:
                res =  values[m][1]
                l = m + 1
        return res