# 给你一个由小写字母组成的字符串 s ，和一个整数 k 。如果满足下述条件，则可以将字符串 t 视作是 理想字符串 ：
#
# t 是字符串 s 的一个子序列。
# t 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 k 。
# 返回 最长 理想字符串的长度。
#
# 字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。
#
# 注意：字母表顺序不会循环。例如，'a' 和 'z' 在字母表中位次的绝对差值是 25 ，而不是 1 。
#
#
#
# 示例 1：
#
# 输入：s = "acfgbd", k = 2
# 输出：4
# 解释：最长理想字符串是 "acbd" 。该字符串长度为 4 ，所以返回 4 。
# 注意 "acfgbd" 不是理想字符串，因为 'c' 和 'f' 的字母表位次差值为 3 。
# 示例 2：
#
# 输入：s = "abcd", k = 3
# 输出：4
# 解释：最长理想字符串是 "abcd" ，该字符串长度为 4 ，所以返回 4 。
#
#
# 提示：
#
# 1 <= s.length <= 105
# 0 <= k <= 25
# s 由小写英文字母组成


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

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        for i in range(n):
            begin, end = max(0, ord(s[i]) - ord('a') - k), min(26, ord(s[i]) - ord('a') + k + 1)
            dp[ord(s[i]) - ord('a')] = max(dp[begin: end]) + 1
        return max(dp)



so = Solution()
print(so.longestIdealString("pvjcci", 4)) # 2
print(so.longestIdealString(s = "abcd", k = 0))
print(so.longestIdealString(s = "xyz", k = 2))
print(so.longestIdealString(s = "acfgbd", k = 2))
print(so.longestIdealString(s = "abcd", k = 3))




