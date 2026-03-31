class LRUCache:
    # built-in data struture OrderedDict
    def __init__(self, capacity: int):
        self.dict_ = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict_:
            return -1
        self.dict_.move_to_end(key)
        return self.dict_[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict_:
            self.dict_[key] = value
            self.dict_.move_to_end(key)
        else:
            self.dict_[key] = value
        if len(self.dict_) > self.capacity:
            self.dict_.popitem(last=False)
        
