# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。
# 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
#
# 示例 1：
#
# 输入：cards = [1,2,8,9], cnt = 3
#
# 输出：18
#
# 解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。
#
# 示例 2：
#
# 输入：cards = [3,3,1], cnt = 1
#
# 输出：0
#
# 解释：不存在获取有效得分的卡牌方案。
#
# 提示：
#
# 1 <= cnt <= cards.length <= 10^5
# 1 <= cards[i] <= 1000
#
# https://leetcode.cn/problems/uOAnQW



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
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        n = len(cards)
        s = sum(cards[n - cnt:])
        if s & 1 == 0:
            return s

        odd, even = -1, -1
        for i in range(n - cnt, n):
            if i != -1 and cards[i] & 1 == 0 and even == -1:
                even = i
            elif i != -1 and cards[i] & 1 == 1 and odd == -1:
                odd = i
        s1, s2 = 0, 0
        for i in range(n - cnt - 1, -1, -1):
            if cards[i] & 1 == 0 and odd != -1 and s1 == 0:
                s1 = s - cards[odd] + cards[i]
            elif cards[i] & 1 == 1 and even != -1 and s2 == 0:
                s2 = s - cards[even] + cards[i]
            if s1 and s2:
                return max(s1, s2)
        return max(s1, s2)


so = Solution()
print(so.maxmiumScore(cards = [7,6,4,6], cnt = 1))
print(so.maxmiumScore(cards = [3,1,6,9,2,4,9,2,3], cnt = 4))
print(so.maxmiumScore(cards = [1,2,8,9], cnt = 3))
print(so.maxmiumScore(cards = [3,3,1], cnt = 1))




