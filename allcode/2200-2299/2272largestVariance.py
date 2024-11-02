# 字符串的 波动 定义为子字符串中出现次数 最多 的字符次数与出现次数 最少 的字符次数之差。
#
# 给你一个字符串 s ，它只包含小写英文字母。请你返回 s 里所有 子字符串的 最大波动 值。
#
# 子字符串 是一个字符串的一段连续字符序列。
#
#  
#
# 示例 1：
#
# 输入：s = "aababbb"
# 输出：3
# 解释：
# 所有可能的波动值和它们对应的子字符串如以下所示：
# - 波动值为 0 的子字符串："a" ，"aa" ，"ab" ，"abab" ，"aababb" ，"ba" ，"b" ，"bb" 和 "bbb" 。
# - 波动值为 1 的子字符串："aab" ，"aba" ，"abb" ，"aabab" ，"ababb" ，"aababbb" 和 "bab" 。
# - 波动值为 2 的子字符串："aaba" ，"ababbb" ，"abbb" 和 "babb" 。
# - 波动值为 3 的子字符串 "babbb" 。
# 所以，最大可能波动值为 3 。
# 示例 2：
#
# 输入：s = "abcde"
# 输出：0
# 解释：
# s 中没有字母出现超过 1 次，所以 s 中每个子字符串的波动值都是 0 。
#  
#
# 提示：
#
# 1 <= s.length <= 104
# s  只包含小写英文字母。


# Map = [['U' for _ in range(n)] for _ in range(m)]

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def largestVariance(self, s: str) -> int:
        s = list(s)
        counter = Counter(s)
        n = len(counter)
        if n == 1:
            return 0
        type = [k for k in counter]
        def maxSubSum(l):

        def helper(a, b):
            new = [0] * len(s)
            for i in range(len(s)):
                if s[i] == a:
                    new[i] = 1
                elif s[i] == b:
                    new[i] = -1
            return maxSubSum(new)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans = max(ans, helper(type[i], type[j]))
                ans = max(ans, helper(type[j], type[i]))
        return ans




so = Solution()
print(so.largestVariance("aababbb"))




