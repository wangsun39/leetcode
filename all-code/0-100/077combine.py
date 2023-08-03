# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= n <= 20
# 1 <= k <= n
from functools import cache
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # ans = []
        @cache
        def dfs(u, v): # 从前 u 个数开始，取 v 个数
            if v == 0: return []
            if u == v:
                return [[i for i in range(1, u + 1)]]
            arr = dfs(u - 1, v - 1)
            if len(arr):
                res = [[u] + x for x in arr]
            else:
                res = [[u]]
            arr = dfs(u - 1, v)
            res += arr
            return res
        return dfs(n, k)





so = Solution()
print(so.combine(n = 4, k = 2))

