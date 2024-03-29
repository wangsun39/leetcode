# 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
#
# 如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
#
#  
#
# 示例 1：
#
# 输入：a = 12, b = 6
# 输出：4
# 解释：12 和 6 的公因子是 1、2、3、6 。
# 示例 2：
#
# 输入：a = 25, b = 30
# 输出：2
# 解释：25 和 30 的公因子是 1、5 。
#  
#
# 提示：
#
# 1 <= a, b <= 1000
#
# https://leetcode.cn/problems/number-of-common-factors

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
    def commonFactors(self, a: int, b: int) -> int:
        m = min(a, b)
        ans = 0
        for i in range(1, m + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans


so = Solution()
print(so.commonFactors(a = 12, b = 6))
print(so.commonFactors(a = 25, b = 30))




