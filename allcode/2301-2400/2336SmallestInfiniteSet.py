# 现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。
#
# 实现 SmallestInfiniteSet 类：
#
# SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
# int popSmallest() 移除 并返回该无限集中的最小整数。
# void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。
#  
#
# 示例：
#
# 输入
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# 输出
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# 解释
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
# smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。
# smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
# smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，
#                                    // 且 1 是最小的整数，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。
#  
#
# 提示：
#
# 1 <= num <= 1000
# 最多调用 popSmallest 和 addBack 方法 共计 1000 次


from typing import List
from typing import Optional
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

class SmallestInfiniteSet1:

    def __init__(self):
        self.s = set([i for i in range(1, 1200)])


    def popSmallest(self) -> int:
        m = min(self.s)
        self.s.remove(m)
        return m



    def addBack(self, num: int) -> None:
        self.s.add(num)


from sortedcontainers import SortedList
class SmallestInfiniteSet:
    # 2023/11/29 优先队列

    def __init__(self):
        self.sl = SortedList(range(1, 1001))


    def popSmallest(self) -> int:
        return self.sl.pop(0)


    def addBack(self, num: int) -> None:
        if num not in self.sl:
            self.sl.add(num)






