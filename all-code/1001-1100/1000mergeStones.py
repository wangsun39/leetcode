# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
#
# 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
#
# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：stones = [3,2,4,1], K = 2
# 输出：20
# 解释：
# 从 [3, 2, 4, 1] 开始。
# 合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
# 合并 [4, 1]，成本为 5，剩下 [5, 5]。
# 合并 [5, 5]，成本为 10，剩下 [10]。
# 总成本 20，这是可能的最小值。
# 示例 2：
#
# 输入：stones = [3,2,4,1], K = 3
# 输出：-1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
# 示例 3：
#
# 输入：stones = [3,5,1,2,6], K = 3
# 输出：25
# 解释：
# 从 [3, 5, 1, 2, 6] 开始。
# 合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
# 合并 [3, 8, 6]，成本为 17，剩下 [17]。
# 总成本 25，这是可能的最小值。
#
#
# 提示：
#
# 1 <= stones.length <= 30
# 2 <= K <= 30
# 1 <= stones[i] <= 100


from typing import List
from math import *
from collections import Counter
from functools import cache
from itertools import accumulate

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        s = list(accumulate(stones, initial=0))
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        @cache
        def dfs(i, j, p):  # 区间 [i, j] 上，合并成p堆的最小代价
            if p == 1:
                if i == j: return 0
                return dfs(i, j, k) + (s[j + 1] - s[i])
            res = inf
            for ii in range(i, j, k - 1):
                res = min(res, dfs(i, ii, 1) + dfs(ii + 1, j, p - 1))
                # ii += 1
            return res
        return dfs(0, n - 1, 1)






obj = Solution()
print(obj.mergeStones([95,54,31,48,44,96,99,20,51,54,18,85,25,84,91,48,40,72,22], 2))
print(obj.mergeStones(stones = [3,2,4,1], k = 2))

