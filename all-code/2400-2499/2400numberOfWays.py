# 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。
#
# 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。
#
# 如果所执行移动的顺序不完全相同，则认为两种方法不同。
#
# 注意：数轴包含负整数。
#
#  
#
# 示例 1：
#
# 输入：startPos = 1, endPos = 2, k = 3
# 输出：3
# 解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
# - 1 -> 2 -> 3 -> 2.
# - 1 -> 2 -> 1 -> 2.
# - 1 -> 0 -> 1 -> 2.
# 可以证明不存在其他方法，所以返回 3 。
# 示例 2：
#
# 输入：startPos = 2, endPos = 5, k = 10
# 输出：0
# 解释：不存在从 2 到 5 且恰好移动 10 步的方法。
#  
#
# 提示：
#
# 1 <= startPos, endPos, k <= 1000


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

import string
# string.digits  表示 0123456789

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = int(1e9 + 7)
        # dp = defaultdict(set)
        # dp[(endPos, 0)] = 1

        @lru_cache(None)
        def helper(pos, step):
            if step == 0:
                return 1 if pos == endPos else 0
            ans = helper(pos - 1, step - 1) + helper(pos + 1, step - 1)
            ans %= MOD
            return ans
        return helper(startPos, k)



so = Solution()
print(so.numberOfWays(startPos = 1, endPos = 2, k = 3))
print(so.numberOfWays(startPos = 2, endPos = 5, k = 10))




