# 现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。
#
# 给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。
#
#  
#
# 示例 1：
#
# 输入：amount = [1,4,2]
# 输出：4
# 解释：下面给出一种方案：
# 第 1 秒：装满一杯冷水和一杯温水。
# 第 2 秒：装满一杯温水和一杯热水。
# 第 3 秒：装满一杯温水和一杯热水。
# 第 4 秒：装满一杯温水。
# 可以证明最少需要 4 秒才能装满所有杯子。
# 示例 2：
#
# 输入：amount = [5,4,4]
# 输出：7
# 解释：下面给出一种方案：
# 第 1 秒：装满一杯冷水和一杯热水。
# 第 2 秒：装满一杯冷水和一杯温水。
# 第 3 秒：装满一杯冷水和一杯温水。
# 第 4 秒：装满一杯温水和一杯热水。
# 第 5 秒：装满一杯冷水和一杯热水。
# 第 6 秒：装满一杯冷水和一杯温水。
# 第 7 秒：装满一杯热水。
# 示例 3：
#
# 输入：amount = [5,0,0]
# 输出：5
# 解释：每秒装满一杯冷水。
#  
#
# 提示：
#
# amount.length == 3
# 0 <= amount[i] <= 100

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

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # amount.sort(reverse=True)
        # if amount[0] >= amount[1] + amount[2]:
        #     return amount[0]
        # s2 = amount[2] - amount[0] // 2
        # s1 = amount[1] - (amount[0] - amount[0] // 2)
        # if s2 < 0:
        #     return amount[0] + s1 + s2
        # return amount[0] + max(s1, s2)

        # amount.sort()
        # if amount[2] >= amount[1] + amount[0]:
        #     return amount[2]
        # x = amount[0] // 2
        # y = amount[0] - x
        # s2, s3 = amount[1] - x, amount[2] - y
        # return amount[0] + max(s2, s3)

        s = sum(amount)
        m = max(amount)
        return max((s + 1) // 2, m)

    def fillCups1(self, amount: List[int]) -> int:  # 另一种解法，包含了实现方法
        amount.sort()
        n1, n2, n3 = amount[0], amount[1], amount[2]
        if n1 + n2 <= n3:
            return n3
        delta = n1 + n2 - n3
        t = delta // 2
        return n3 + t + 1 if delta % 2 == 1 else n3 + t





so = Solution()
print(so.fillCups([7,4,9]))  # 10
print(so.fillCups([2,4,2]))  # 4
print(so.fillCups([2,4,4]))  # 5
print(so.fillCups([5,4,4]))  # 7
print(so.fillCups([4,1,4]))  # 5
print(so.fillCups([1,4,2]))  # 4
print(so.fillCups([5,0,0]))  # 5




