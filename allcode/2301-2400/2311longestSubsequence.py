# 给你一个二进制字符串 s 和一个正整数 k 。
#
# 请你返回 s 的 最长 子序列，且该子序列对应的 二进制 数字小于等于 k 。
#
# 注意：
#
# 子序列可以有 前导 0 。
# 空字符串视为 0 。
# 子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
#  
#
# 示例 1：
#
# 输入：s = "1001010", k = 5
# 输出：5
# 解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
# 注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
# 最长子序列的长度为 5 ，所以返回 5 。
# 示例 2：
#
# 输入：s = "00101001", k = 1
# 输出：6
# 解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
# 最长子序列的长度为 6 ，所以返回 6 。
#  
#
# 提示：
#
# 1 <= s.length <= 1000
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= k <= 109

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
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

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0:
            return 0
        value = int(s, 2)
        # print(value)
        ans = n
        pos = []
        for i, e in enumerate(s):
            if e == '1':
                pos.append(i)
        i = 0
        bias = 0
        if value <= k:
            return ans
        while i < len(pos): # 从左至右，依次把s中的1删掉，第一个满足<=k的就是答案
            s = s[:pos[i] - bias] + s[pos[i] - bias + 1:]
            value = int(s, 2)
            ans -= 1
            if value <= k:
                return ans
            bias += 1
            i += 1
        return ans



so = Solution()
print(so.longestSubsequence(s = "1001010", k = 5))
print(so.longestSubsequence(s = "00101001", k = 1))
print(so.longestSubsequence(s = "", k = 5))
print(so.longestSubsequence(s = "00101001", k = 0))




