class TimeMap:

    def __init__(self):
        self.kv = OrderedDict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kv:
            L, R = 0, len(self.kv[key]) - 1
            while L <= R:
                M = (L + R) // 2
                if self.kv[key][M][0] < timestamp:
                    L = M + 1
                elif self.kv[key][M][0] > timestamp:
                    R = M - 1
                else:
                    return self.kv[key][M][1]

            return self.kv[key][R][1] if R>=0 else ""
        else:
            return ""
