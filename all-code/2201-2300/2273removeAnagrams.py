
# Map = [['U' for _ in range(n)] for _ in range(m)]

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = set()
        ans = []
        def helper(words):
            n = len(words)
            if n <= 1:
                return words
            n1, n2 = ''.join(sorted(list(words[-1]))), ''.join(sorted(list(words[-2])))
            if n1 == n2:
                return helper(words[:n - 1])
            return helper(words[:n - 1]) + [words[-1]]
        return helper(words)



so = Solution()
print(so.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print(so.removeAnagrams(["a","b","a"]))
print(so.removeAnagrams(["a","b","c","d","e"]))




