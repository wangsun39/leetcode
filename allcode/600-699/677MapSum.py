class MapSum1:
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

class Trie:

    def __init__(self):
        self.root = {'sum': 0, 'self': 0}   # cnt 表示以当前节点为前缀的单词有多少个，'end' 表示以当前前缀作为单词的有多少个

    def insert(self, word: str, val) -> None:  # O(log(len(word)))
        cur = self.root
        def dfs(i, cur):
            if i == len(word):
                old = cur['self']
                cur['self'] = val
                cur['sum'] += val - old
                return val - old  # 返回差值
            if word[i] not in cur:
                cur[word[i]] = {'sum': 0, 'self': 0}
            diff = dfs(i + 1, cur[word[i]])
            cur['sum'] += diff
            return diff
        dfs(0, cur)

    def startsWith(self, prefix: str) -> [str]:
        # 返回以前缀开头的所有词的和
        cur = self.root
        def dfs(i, cur):
            if i == len(prefix):
                return cur['sum']
            if prefix[i] not in cur:
                return 0
            return dfs(i + 1, cur[prefix[i]])
        return dfs(0, cur)

# 2025/10/22  Trie
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tr = Trie()


    def insert(self, key: str, val: int) -> None:
        self.tr.insert(key, val)


    def sum(self, prefix: str) -> int:
        return self.tr.startsWith(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
obj = MapSum()
obj.insert("apple",3)
print(obj.sum("ap"))
obj.insert("app",2)
obj.insert("apple",2)
print(obj.sum("ap"))
