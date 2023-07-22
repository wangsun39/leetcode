# 给你两个字符串数组 event1 和 event2 ，表示发生在同一天的两个闭区间时间段事件，其中：
#
# event1 = [startTime1, endTime1] 且
# event2 = [startTime2, endTime2]
# 事件的时间为有效的 24 小时制且按 HH:MM 格式给出。
#
# 当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 冲突 。
#
# 如果两个事件之间存在冲突，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
# 输出：true
# 解释：两个事件在 2:00 出现交集。
# 示例 2：
#
# 输入：event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
# 输出：true
# 解释：两个事件的交集从 01:20 开始，到 02:00 结束。
# 示例 3：
#
# 输入：event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
# 输出：false
# 解释：两个事件不存在交集。
#
#
# 提示：
#
# evnet1.length == event2.length == 2.
# event1[i].length == event2[i].length == 5
# startTime1 <= endTime1
# startTime2 <= endTime2
# 所有事件的时间都按照 HH:MM 格式给出
# https://leetcode.cn/problems/determine-if-two-events-have-conflict/

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
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event1[0] > event2[0]:
            event1, event2 = event2, event1
        if event1[1] >= event2[0]:
            return True
        return False


so = Solution()
print(so.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))
print(so.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))
print(so.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]))




