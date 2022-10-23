# 共有 n 位员工，每位员工都有一个从 0 到 n - 1 的唯一 id 。
#
# 给你一个二维整数数组 logs ，其中 logs[i] = [idi, leaveTimei] ：
#
# idi 是处理第 i 个任务的员工的 id ，且
# leaveTimei 是员工完成第 i 个任务的时刻。所有 leaveTimei 的值都是 唯一 的。
# 注意，第 i 个任务在第 (i - 1) 个任务结束后立即开始，且第 0 个任务从时刻 0 开始。
#
# 返回处理用时最长的那个任务的员工的 id 。如果存在两个或多个员工同时满足，则返回几人中 最小 的 id 。
#
#
#
# 示例 1：
#
# 输入：n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
# 输出：1
# 解释：
# 任务 0 于时刻 0 开始，且在时刻 3 结束，共计 3 个单位时间。
# 任务 1 于时刻 3 开始，且在时刻 5 结束，共计 2 个单位时间。
# 任务 2 于时刻 5 开始，且在时刻 9 结束，共计 4 个单位时间。
# 任务 3 于时刻 9 开始，且在时刻 15 结束，共计 6 个单位时间。
# 时间最长的任务是任务 3 ，而 id 为 1 的员工是处理此任务的员工，所以返回 1 。
# 示例 2：
#
# 输入：n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
# 输出：3
# 解释：
# 任务 0 于时刻 0 开始，且在时刻 1 结束，共计 1 个单位时间。
# 任务 1 于时刻 1 开始，且在时刻 7 结束，共计 6 个单位时间。
# 任务 2 于时刻 7 开始，且在时刻 12 结束，共计 5 个单位时间。
# 任务 3 于时刻 12 开始，且在时刻 17 结束，共计 5 个单位时间。
# 时间最长的任务是任务 1 ，而 id 为 3 的员工是处理此任务的员工，所以返回 3 。
# 示例 3：
#
# 输入：n = 2, logs = [[0,10],[1,20]]
# 输出：0
# 解释：
# 任务 0 于时刻 0 开始，且在时刻 10 结束，共计 10 个单位时间。
# 任务 1 于时刻 10 开始，且在时刻 20 结束，共计 10 个单位时间。
# 时间最长的任务是任务 0 和 1 ，处理这两个任务的员工的 id 分别是 0 和 1 ，所以返回最小的 0 。
#
#
# 提示：
#
# 2 <= n <= 500
# 1 <= logs.length <= 500
# logs[i].length == 2
# 0 <= idi <= n - 1
# 1 <= leaveTimei <= 500
# idi != idi + 1
# leaveTimei 按严格递增顺序排列
# https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task/

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
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
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

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = logs[0][0]
        val = logs[0][1]
        for i, [id, t] in enumerate(logs[1:], 1):
            if t - logs[i - 1][1] > val:
                ans = id
                val = t - logs[i - 1][1]
            elif t - logs[i - 1][1] == val:
                ans = min(ans, id)
        return ans


so = Solution()
print(so.hardestWorker(70,
[[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))
print(so.hardestWorker(n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]))
print(so.hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]))
print(so.hardestWorker(n = 2, logs = [[0,10],[1,20]]))




