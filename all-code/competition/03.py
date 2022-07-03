
from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        N = int(1e9 + 7)
        f = [0] * n
        g = [0] * n
        for i in range(delay):
            f[i] = 1
        g[0] = 1
        for i in range(delay, forget):
            g[i] = sum(g[:i - delay + 1]) % N
            f[i] = (g[i] + f[i - 1]) % N
        for i in range(forget, n):
            s = 0
            for j in range(i - forget + 1, i - delay + 1):
                s += g[j]
                s %= N
            g[i] = s
            f[i] = (g[i] - g[i - forget] + f[i - 1]) % N
        print(g)
        print(f)
        return f[-1]


so = Solution()
print(so.peopleAwareOfSecret(n = 7, delay = 3, forget = 5))
print(so.peopleAwareOfSecret(n = 6, delay = 2, forget = 4))
print(so.peopleAwareOfSecret(n = 4, delay = 1, forget = 3))




