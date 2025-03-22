
from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)



class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True


    def search(self, word: str) -> bool:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return 'end' in cur



    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
            else:
                return False
        return True


# 计数的Trie树
class Trie:

    def __init__(self):
        self.root = {'cnt': 0, 'end': 0}   # cnt 表示以当前节点为前缀的单词有多少个，'end' 表示以当前前缀作为单词的有多少个

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {'cnt': 1}
            else:
                cur[e]['cnt'] += 1
            cur = cur[e]
        if 'end' not in cur:
            cur['end'] = 1
        else:
            cur['end'] += 1
        # cur['cnt'] += 1
        self.root['cnt'] += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for e in word:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        if 'end' in cur:
            return cur['end']
        return 0

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
            else:
                return 0
        return cur['cnt']

    def erase(self, word: str) -> None:
        cur = self.root
        for i, e in enumerate(word):
            if cur[e]['cnt'] == 1:
                del(cur[e])
                return
            else:
                cur[e]['cnt'] -= 1
                if i == len(word) - 1:
                    break
            cur = cur[e]
        cur[e]['end'] -= 1
        self.root['cnt'] -= 1

    def startsWith(self, prefix: str) -> [str]:
        # 返回以前缀开头的所有词
        cur = self.root
        for e in prefix:
            if e in cur:
                cur = cur[e]
                if 'end' in cur:
                    return [x for x in cur if x != 'end']
            else:
                return []

        def dfs(node):
            if 'end' in node:
                return ['']
            res = []
            for x in node:
                l = dfs(node[x])
                res += [x + st for st in l]
            return res
        res = dfs(cur)
        return [prefix + x for x in res]


