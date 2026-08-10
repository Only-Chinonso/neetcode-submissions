class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(cache) > capacity:
                del cache[list(cache)[-1]]
                self.cache[key] = value
