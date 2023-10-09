# 给你区间的 空 集，请你设计并实现满足要求的数据结构：
#
# 新增：添加一个区间到这个区间集合中。
# 统计：计算出现在 至少一个 区间中的整数个数。
# 实现 CountIntervals 类：
#
# CountIntervals() 使用区间的空集初始化对象
# void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
# int count() 返回出现在 至少一个 区间中的整数个数。
# 注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。
#
#  
#
# 示例 1：
#
# 输入
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# 输出
# [null, null, null, 6, null, 8]
#
# 解释
# CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
# countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
# countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
# countIntervals.count();    // 返回 6
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 7、8、9、10 出现在区间 [7, 10] 中
# countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
# countIntervals.count();    // 返回 8
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 5 和 6 出现在区间 [5, 8] 中
#                            // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
#                            // 整数 9 和 10 出现在区间 [7, 10] 中
#  
#
# 提示：
#
# 1 <= left <= right <= 109
# 最多调用  add 和 count 方法 总计 105 次
# 调用 count 方法至少一次


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

class CountIntervals:

    def __init__(self):
        self.total = 0
        self.left = []
        self.right = []


    def add(self, left: int, right: int) -> None:
        pos = bisect.bisect_left(self.right, left - 1)
        if 0 == len(self.left) or left > self.right[-1]:
            self.left.append(left)
            self.right.append(right)
            self.total += (right - left + 1)
            return
        if right < self.left[0] - 1:
            self.left.insert(0, left)
            self.right.insert(0, right)
            self.total += (right - left + 1)

        L, R = left, right
        duplicate = 0
        while pos < len(self.left) and R >= self.left[pos] - 1: # merge section
            L = min(L, self.left[pos])
            R = max(R, self.right[pos])
            duplicate += (self.right[pos] - self.left[pos] + 1)
            del(self.left[pos])
            del (self.right[pos])

        self.total += (R - L + 1 - duplicate)
        self.left.insert(pos, L)
        self.right.insert(pos, R)
        # print(self.left)
        # print(self.right)
        # print(self.total)

    def count(self) -> int:
        return self.total


so = CountIntervals()
so.add(457, 717)
so.add(918,927)
print(so.count())
so.add(660,675)
print(so.count())
so.add(885,905)
# so.add(323,416)
# so.add(774,808)
print(so.count())
so.add(5, 8)
print(so.count())

so = CountIntervals()
so.add(8, 43)
so.add(13, 16)
print(so.count())
so.add(5, 8)
print(so.count())

# so = CountIntervals()
# so.add(2, 3)
# so.add(7, 10)
# print(so.count())
# so.add(5, 8)
# print(so.count())



