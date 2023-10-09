# 给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, pricei] 表示你可以以 pricei 元的价格卖一块高为 hi 宽为 wi 的矩形木块。
#
# 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
#
# 沿垂直方向按高度 完全 切割木块，或
# 沿水平方向按宽度 完全 切割木块
# 在将一块木块切成若干小木块后，你可以根据 prices 卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能 旋转切好后木块的高和宽。
#
# 请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
#
# 注意你可以切割木块任意次。
#
#  
#
# 示例 1：
#
#
#
# 输入：m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
# 输出：19
# 解释：上图展示了一个可行的方案。包括：
# - 2 块 2 x 2 的小木块，售出 2 * 7 = 14 元。
# - 1 块 2 x 1 的小木块，售出 1 * 3 = 3 元。
# - 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
# 总共售出 14 + 3 + 2 = 19 元。
# 19 元是最多能得到的钱数。
# 示例 2：
#
#
#
# 输入：m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
# 输出：32
# 解释：上图展示了一个可行的方案。包括：
# - 3 块 3 x 2 的小木块，售出 3 * 10 = 30 元。
# - 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
# 总共售出 30 + 2 = 32 元。
# 32 元是最多能得到的钱数。
# 注意我们不能旋转 1 x 4 的木块来得到 4 x 1 的木块。
#  
#
# 提示：
#
# 1 <= m, n <= 200
# 1 <= prices.length <= 2 * 104
# prices[i].length == 3
# 1 <= hi <= m
# 1 <= wi <= n
# 1 <= pricei <= 106
# 所有 (hi, wi) 互不相同 。

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
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(length, width):
            if length < ls[0] or width < ws[0]:
                return 0
            ans = d[(length, width)]
            for i in range(1, length):
                ans = max(ans, dfs(i, width) + dfs(length - i, width))
            for i in range(1, width):
                ans = max(ans, dfs(length, i) + dfs(length, width - i))
            return ans
        d = defaultdict(int)
        for e in prices:
            d[(e[0], e[1])] = e[2]

        ls, ws = [e[0] for e in prices], [e[1] for e in prices]
        ls.sort()
        ws.sort()
        return dfs(m, n)


so = Solution()
print(so.sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]))
print(so.sellingWood(m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]))




