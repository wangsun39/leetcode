# 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。
#
# MK 平均值 按照如下步骤计算：
#
# 如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
# 从这个容器中删除最小的 k 个数和最大的 k 个数。
# 计算剩余元素的平均值，并 向下取整到最近的整数 。
# 请你实现 MKAverage 类：
#
# MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
# void addElement(int num) 往数据流中插入一个新的元素 num 。
# int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
#
#
# 示例 1：
#
# 输入：
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# 输出：
# [null, null, null, -1, null, 3, null, null, null, 5]
#
# 解释：
# MKAverage obj = new MKAverage(3, 1);
# obj.addElement(3);        // 当前元素为 [3]
# obj.addElement(1);        // 当前元素为 [3,1]
# obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
# obj.addElement(10);       // 当前元素为 [3,1,10]
# obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
#                           // 删除最小以及最大的 1 个元素后，容器为 [3]
#                           // [3] 的平均值等于 3/1 = 3 ，故返回 3
# obj.addElement(5);        // 当前元素为 [3,1,10,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
# obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
#                           // 删除最小以及最大的 1 个元素后，容器为 [5]
#                           // [5] 的平均值等于 5/1 = 5 ，故返回 5
#
#
# 提示：
#
# 3 <= m <= 105
# 1 <= k*2 < m
# 1 <= num <= 105
# addElement 与 calculateMKAverage 总操作次数不超过 105 次。





from typing import List
from heapq import *
from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.last_m = deque([])  # 最近放入的 m 个数字
        self.sorted_m = SortedList([])
        self.sum = 0
        self.lo, self.hi = self.k, self.m - self.k - 1  # 中间部分为下标区间[self.lo, self.hi]
        self.mid_sum = 0  # 中间部分的数据和，除去头尾各k个元素

    def addElement(self, num: int) -> None:
        if len(self.last_m) < self.m:
            self.last_m.append(num)
            self.sorted_m.add(num)
            if len(self.last_m) == self.m:
                self.mid_sum = sum(self.sorted_m[self.lo: self.hi + 1])
            return
        oldest = self.last_m[0]
        if oldest < self.sorted_m[self.lo]:
            self.mid_sum -= self.sorted_m[self.lo]
        elif oldest > self.sorted_m[self.hi]:
            self.mid_sum -= self.sorted_m[self.hi]
        else:
            self.mid_sum -= oldest
        self.sorted_m.remove(oldest)
        self.last_m.popleft()

        if num < self.sorted_m[self.lo - 1]:
            self.mid_sum += (self.sorted_m[self.lo - 1])
        elif num > self.sorted_m[-self.k]:
            self.mid_sum += (self.sorted_m[-self.k])
        else:
            self.mid_sum += num
        self.sorted_m.add(num)
        self.last_m.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.last_m) < self.m:
            return -1
        return self.mid_sum // (self.m - 2 * self.k)


so = MKAverage(3, 1)

print(so.addElement(58916))
print(so.addElement(61899))
print(so.calculateMKAverage())
print(so.addElement(85406))
print(so.addElement(49757))
print(so.calculateMKAverage())
print(so.addElement(27520))
print(so.addElement(12303))
print(so.calculateMKAverage())
print(so.addElement(63945))
# print(so.calculateMKAverage())


so = MKAverage(3, 1)

print(so.addElement(3))
print(so.addElement(1))
print(so.calculateMKAverage())
print(so.addElement(10))
print(so.calculateMKAverage())
print(so.addElement(5))
print(so.addElement(5))
print(so.addElement(5))
print(so.calculateMKAverage())




