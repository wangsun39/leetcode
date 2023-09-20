# 给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示 闭 区间 [lefti, righti] 。
#
# 你需要将 intervals 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。
#
# 请你返回 最少 需要划分成多少个组。
#
# 如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 [1, 5] 和 [5, 8] 相交。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# 输出：3
# 解释：我们可以将区间划分为如下的区间组：
# - 第 1 组：[1, 5] ，[6, 8] 。
# - 第 2 组：[2, 3] ，[5, 10] 。
# - 第 3 组：[1, 10] 。
# 可以证明无法将区间划分为少于 3 个组。
# 示例 2：
#
# 输入：intervals = [[1,3],[5,6],[8,10],[11,13]]
# 输出：1
# 解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。
#  
#
# 提示：
#
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 106


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
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

class Solution:
    def minGroups1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        group = [intervals[0][1]]
        for iv in intervals[1:]:
            if len(group) > 0 and group[0] < iv[0]:
                del(group[0])
                bisect.insort_right(group, iv[1])
            else:
                bisect.insort_right(group, iv[1])
        return len(group)

    def minGroups2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        for it in intervals[1:]:
            if heap[0] >= it[0]:
                heapq.heappush(heap, it[1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, it[1])
        return len(heap)


    def minGroups(self, intervals: List[List[int]]) -> int:
        # 2023/9/19  差分数组
        mx = max(x[1] for x in intervals) + 1
        diff = [0] * mx
        for a, b in intervals:
            diff[a - 1] += 1
            diff[b] -= 1
        ans = cur = 0
        for x in diff:
            cur += x
            if cur > ans:
                ans = cur
        return ans

so = Solution()
print(so.minGroups([[1,3],[5,6],[8,10],[11,13]]))
print(so.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))




