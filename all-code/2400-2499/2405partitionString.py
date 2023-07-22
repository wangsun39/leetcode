# 给你一个字符串 s ，请你将该字符串划分成一个或多个 子字符串 ，并满足每个子字符串中的字符都是 唯一 的。也就是说，在单个子字符串中，字母的出现次数都不超过 一次 。
#
# 满足题目要求的情况下，返回 最少 需要划分多少个子字符串。
#
# 注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。
#
#  
#
# 示例 1：
#
# 输入：s = "abacaba"
# 输出：4
# 解释：
# 两种可行的划分方法分别是 ("a","ba","cab","a") 和 ("ab","a","ca","ba") 。
# 可以证明最少需要划分 4 个子字符串。
# 示例 2：
#
# 输入：s = "ssssss"
# 输出：6
# 解释：
# 只存在一种可行的划分方法 ("s","s","s","s","s","s") 。
#  
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由小写英文字母组成


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
    def partitionString(self, s: str) -> int:
        counter = set(s[0])
        ans = 1
        for ss in s[1:]:
            if ss in counter:
                ans += 1
                counter = set(ss)
            else:
                counter.add(ss)
        return ans


so = Solution()
print(so.partitionString("abacaba"))
print(so.partitionString("ssssss"))




