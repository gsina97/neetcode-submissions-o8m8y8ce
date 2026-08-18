class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache[key]
        if not values:
            return ""

        l = 0
        r = len(values) - 1

        # stores timestamps
        res = -1
        while r >= l:
            m = (l + r) // 2
            val = values[m]

            if val[1] == timestamp:
                return val[0]
            elif val[1] > timestamp:
                r = m - 1
            else:
                res = m
                l = m + 1
        return values[res][0] if res != -1 else ""
        


# map word to list, 