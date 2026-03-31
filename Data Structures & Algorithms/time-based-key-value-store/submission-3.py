class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.items:
            self.items[key].append((timestamp, value))
        else:
            self.items[key]=[(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items.keys():
            return ""
        l, r = 0, len(self.items[key])-1
        while l<=r:
            m=l+(r-l)//2
            if self.items[key][m][0]<timestamp:
                l = m+1
            elif self.items[key][m][0]>timestamp:
                r = m-1
            else:
                return self.items[key][m][1]
        min_ = min(l, r)
        return self.items[key][min_][1] if min_>=0 else ""

