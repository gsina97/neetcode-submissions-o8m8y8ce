class TimeMap:

    def __init__(self):
        # key -> (val, ts)
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.cache.get(key, [])

        l = 0
        r = len(values) - 1

        while r >= l:
            m = (l + r  ) // 2

            found_val, found_ts = values[m]
            if found_ts == timestamp:
                res = found_val
                break
            elif found_ts > timestamp:
                r = m -1
            else:
                res = found_val
                l = m + 1
        return res
