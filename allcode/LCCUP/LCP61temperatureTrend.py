# 力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 i ~ (i+1) 天的气温变化趋势，将根据以下规则判断：
#
# 若第 i+1 天的气温 高于 第 i 天，为 上升 趋势
# 若第 i+1 天的气温 等于 第 i 天，为 平稳 趋势
# 若第 i+1 天的气温 低于 第 i 天，为 下降 趋势
# 已知 temperatureA[i] 和 temperatureB[i] 分别表示第 i 天两地区的气温。
# 组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势相同的最大连续天数。
#
# 即最大的 n，使得第 i~i+n 天之间，两地气温变化趋势相同
#
# 示例 1：
#
# 输入：
# temperatureA = [21,18,18,18,31]
# temperatureB = [34,32,16,16,17]
#
# 输出：2
#
# 解释：如下表所示， 第 2～4 天两地气温变化趋势相同，且持续时间最长，因此返回 4-2=2
#
#
# 示例 2：
#
# 输入：
# temperatureA = [5,10,16,-6,15,11,3]
# temperatureB = [16,22,23,23,25,3,-16]
#
# 输出：3
#
# 提示：
#
# 2 <= temperatureA.length == temperatureB.length <= 1000
# -20 <= temperatureA[i], temperatureB[i] <= 40
#
# https://leetcode.cn/problems/6CE719

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
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        ans = 0
        cur = 0
        for i in range(n - 1):
            if (temperatureA[i + 1] - temperatureA[i] > 0 and temperatureB[i + 1] - temperatureB[i] > 0) \
                    or (temperatureA[i + 1] - temperatureA[i] == 0 and temperatureB[i + 1] - temperatureB[
                i] == 0) \
                    or (temperatureA[i + 1] - temperatureA[i] < 0 and temperatureB[i + 1] - temperatureB[
                i] < 0):
                cur += 1
            else:
                cur = 0
                continue
            ans = max(ans, cur)
        return ans




so = Solution()
print(so.temperatureTrend([5,10,16,-6,15,11,3], [16,22,23,23,25,3,-16]))
print(so.temperatureTrend([21,18,18,18,31], [34,32,16,16,17]))




