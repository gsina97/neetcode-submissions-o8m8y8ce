class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        
        values = self.cache[key]

        l = 0
        r = len(values) - 1
        res = ""


        while r >= l:
            m = (l + r) // 2

            tmp = values[m]
            if tmp[1] == timestamp:
                return tmp[0]
            elif tmp[1] > timestamp:
                r = m - 1
            else:
                res = tmp[0]
                l = m + 1
        return res
