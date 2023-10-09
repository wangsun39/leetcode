class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m_map = {}

    def insert(self, key: str, val: int) -> None:
        self.m_map[key] = val
        return None

    def sum(self, prefix: str) -> int:
        sum = 0
        for (key, value) in self.m_map.items():
            if key.startswith(prefix):
                sum += value
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
obj = MapSum()
obj.insert("apple",3)
print(obj.sum("ap"))
obj.insert("app",2)
print(obj.sum("ap"))
