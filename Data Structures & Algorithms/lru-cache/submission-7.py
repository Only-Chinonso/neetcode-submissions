class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.res = set()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.res.remove(key)
            self.res.add(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) > self.capacity:
                del self.cache[self.res[0]]
                self.cache[key] = value
