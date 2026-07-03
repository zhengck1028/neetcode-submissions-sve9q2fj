class TimeMap:

    def __init__(self):
        self.dict_ = defaultdict(list) # [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dict_[key]) - 1
        # [(1, happy), (3, sad)]
        while l <= r:
            m = (l + r) // 2 # 0
            if self.dict_[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return self.dict_[key][l-1][1] if l >= 1 else ""
