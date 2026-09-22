class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.cache[key]

        l = 0
        r = len(values) - 1

        while r >= l:
            m = (l + r) // 2

            val = values[m]

            if val[1] == timestamp:
                res =  val[0]
                break
            elif val[1] > timestamp:
                r = m - 1
            else:
                res = val[0]
                l = m + 1
        return res

        
