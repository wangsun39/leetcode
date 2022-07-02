# 给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
#
# 最好 英文字母的大写和小写形式必须 都 在 s 中出现。
#
# 英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。
#
#  
#
# 示例 1：
#
# 输入：s = "lEeTcOdE"
# 输出："E"
# 解释：
# 字母 'E' 是唯一一个大写和小写形式都出现的字母。
# 示例 2：
#
# 输入：s = "arRAzFif"
# 输出："R"
# 解释：
# 字母 'R' 是大写和小写形式都出现的最好英文字母。
# 注意 'A' 和 'F' 的大写和小写形式也都出现了，但是 'R' 比 'F' 和 'A' 更好。
# 示例 3：
#
# 输入：s = "AbCdEfGhIjK"
# 输出：""
# 解释：
# 不存在大写和小写形式都出现的字母。
#  
#
# 提示：
#
# 1 <= s.length <= 1000
# s 由小写和大写英文字母组成

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
    def greatestLetter(self, s: str) -> str:
        s1, s2 = set(), set()
        for e in s:
            if ord(e) <= ord('Z'):
                s1.add(e)
            else:
                s2.add(chr(ord(e) - 32))
        s = s1 & s2
        if len(s) == 0:
            return ''
        else:
            l = list(s)
            l.sort()
            return l[-1]




so = Solution()
print(so.greatestLetter("lEeTcOdE"))
print(so.greatestLetter("arRAzFif"))
print(so.greatestLetter("AbCdEfGhIjK"))




