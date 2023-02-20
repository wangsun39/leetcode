# 给你一个整数数组 ranks 和一个字符数组 suit 。你有 5 张扑克牌，第 i 张牌大小为 ranks[i] ，花色为 suits[i] 。
#
# 下述是从好到坏你可能持有的 手牌类型 ：
#
# "Flush"：同花，五张相同花色的扑克牌。
# "Three of a Kind"：三条，有 3 张大小相同的扑克牌。
# "Pair"：对子，两张大小一样的扑克牌。
# "High Card"：高牌，五张大小互不相同的扑克牌。
# 请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型 。
#
# 注意：返回的字符串 大小写 需与题目描述相同。
#
#
#
# 示例 1：
#
# 输入：ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
# 输出："Flush"
# 解释：5 张扑克牌的花色相同，所以返回 "Flush" 。
# 示例 2：
#
# 输入：ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
# 输出："Three of a Kind"
# 解释：第一、二和四张牌组成三张相同大小的扑克牌，所以得到 "Three of a Kind" 。
# 注意我们也可以得到 "Pair" ，但是 "Three of a Kind" 是更好的手牌类型。
# 有其他的 3 张牌也可以组成 "Three of a Kind" 手牌类型。
# 示例 3：
#
# 输入：ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
# 输出："Pair"
# 解释：第一和第二张牌大小相同，所以得到 "Pair" 。
# 我们无法得到 "Flush" 或者 "Three of a Kind" 。
#
#
# 提示：
#
# ranks.length == suits.length == 5
# 1 <= ranks[i] <= 13
# 'a' <= suits[i] <= 'd'
# 任意两张扑克牌不会同时有相同的大小和花色。


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
import math
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cr, cs = Counter(ranks), Counter(suits)
        if len(cs) == 1:
            return 'Flush'
        if any(x >= 3 for x in cr.values()):
            return 'Three of a Kind'
        if any(x >= 2 for x in cr.values()):
            return 'Pair'
        if len(cr) == 5:
            return 'High Card'




so = Solution()





