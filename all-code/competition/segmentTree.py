
from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class RangeModule:


    def __init__(self):
        self.tree = defaultdict(int)

    def pushup(self, id: int):
        if (1 == self.tree[id << 1]) and (1 == self.tree[(id << 1) | 1]):
            self.tree[id] = 1
        else:
            self.tree[id] = 0

    def pushdown(self, id: int):
        if self.tree[id]:
            left, right = id << 1, (id << 1) | 1
            self.tree[left] = self.tree[id]
            self.tree[right] = self.tree[id]

    def update(self, id: int, start: int, end: int, l: int, r: int, val: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] = val
            return
        mid = (start + end) >> 1
        self.pushdown(id)
        self.update(id << 1, start, mid, l, r, val)
        self.update((id << 1) | 1, mid + 1, end, l, r, val)
        self.pushup(id)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return True
        if start >= l and end <= r:
            return self.tree[id] == 1
        mid = (start + end) >> 1
        self.pushdown(id)
        left = self.query(id << 1, start, mid, l, r)
        if not left:
            return False
        return self.query((id << 1) | 1, mid + 1, end, l, r)


    def addRange(self, left: int, right: int) -> None:
        self.update(1, 1, 10 ** 9, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(1, 1, 10 ** 9, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(1, 1, 10 ** 9, left, right - 1, 2)


# 2569
class Solution2:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        todo = [False] * (4 * n)  # 特殊区间的lazy标记

        # # 维护区间 1 的个数
        # def maintain(o: int) -> None:
        #     cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]
        #
        # # 执行区间反转
        # def do(o: int, l: int, r: int) -> None:
        #     cnt1[o] = r - l + 1 - cnt1[o]
        #     todo[o] = not todo[o]

        # 初始化线段树   o,l,r=1,1,n
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                # ...
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            # ... maintain(o)

        # 反转区间 [L,R]   o,l,r=1,1,n
        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            # 进入这个函数的前提是，[l,r] 与 [L,R]有交集
            if L <= l and r <= R:
                # ... do(o, l, r)
                return
            m = (l + r) // 2
            # if todo[o]:
            #     do(o * 2, l, m)
            #     do(o * 2 + 1, m + 1, r)
            #     todo[o] = False
            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            # ... maintain(o)

        # build(1, 1, n)
        # ans, s = [], sum(nums2)
        # for op, l, r in queries:
        #     if op == 1: update(1, 1, n, l + 1, r + 1)
        #     elif op == 2: s += l * cnt1[1]
        #     else: ans.append(s)
        # return ans






