# 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。
#
# 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
# 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "abacaba"
# 输出：2
# 解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
# "ab" 是最长的字母序连续子字符串。
# 示例 2：
#
# 输入：s = "abcde"
# 输出：5
# 解释："abcde" 是最长的字母序连续子字符串。
#  
#
# 提示：
#
# 1 <= s.length <= 105
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
# heap.heapify(nums) # 小顶堆
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
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        cur = 1
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 1
        return ans


so = Solution()
print(so.longestContinuousSubstring("abacaba"))
print(so.longestContinuousSubstring("abcde"))




