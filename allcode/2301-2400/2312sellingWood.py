# 给你两个整数m 和n，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组prices，其中prices[i] = [hi, wi, pricei]表示你可以以pricei元的价格卖一块高为hi宽为wi的矩形木块。
#
# 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
#
# 沿垂直方向按高度 完全 切割木块，或
# 沿水平方向按宽度 完全 切割木块
# 在将一块木块切成若干小木块后，你可以根据 prices卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能旋转切好后木块的高和宽。
#
# 请你返回切割一块大小为m x n 的木块后，能得到的最多钱数。
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
# 所有(hi, wi) 互不相同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sellingWood1(self, m: int, n: int, prices: List[List[int]]) -> int:
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


    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # 2024/3/15 稍作一些简化
        d = {}
        for h, w, p in prices:
            d[(h, w)] = p

        @cache
        def dfs(r, c):
            res = 0
            if (r, c) in d:
                res = d[(r, c)]
            for i in range(r // 2):
                res = max(res, dfs(i + 1, c) + dfs(r - i - 1, c))
            for i in range(c // 2):
                res = max(res, dfs(r, i + 1) + dfs(r, c - i - 1))
            return res

        return dfs(m, n)


so = Solution()
print(so.sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]))
print(so.sellingWood(m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]))




