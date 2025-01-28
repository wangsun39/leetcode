# 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：
#
# perm[i] 能够被 i 整除
# i 能够被 perm[i] 整除
# 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：
# 第 1 个优美的排列是 [1,2]：
#     - perm[1] = 1 能被 i = 1 整除
#     - perm[2] = 2 能被 i = 2 整除
# 第 2 个优美的排列是 [2,1]:
#     - perm[1] = 2 能被 i = 1 整除
#     - i = 2 能被 perm[2] = 1 整除
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
# 提示：
#
# 1 <= n <= 15

from typing import List
from collections import defaultdict
import copy

class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [0 for _ in range(1 << n)]
        dp[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count('1')
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    dp[mask] += dp[mask ^ (1 << i)]
        return dp[(1 << n) - 1]




so = Solution()
print(so.findLongestWord('abpcplea', ["ale","apple","monkey","plea"]))
print(so.findLongestWord('abpcplea', ["a","b","c"]))
print(so.findLongestWord("bab", ["ba","ab","a","b"]))

