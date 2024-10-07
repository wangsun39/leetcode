# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
#
# 房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
#
# 假设正方形瓷砖的规格不限，边长都是整数。
#
# 请你帮设计师计算一下，最少需要用到多少块方形瓷砖？
#
#
#
# 示例 1：
#
#
#
# 输入：n = 2, m = 3
# 输出：3
# 解释：3 块地砖就可以铺满卧室。
#      2 块 1x1 地砖
#      1 块 2x2 地砖
# 示例 2：
#
#
#
# 输入：n = 5, m = 8
# 输出：5
# 示例 3：
#
#
#
# 输入：n = 11, m = 13
# 输出：6
#
#
# 提示：
#
# 1 <= n <= 13
# 1 <= m <= 13
from math import inf
from leetcode.allcode.competition.mypackage import *


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        ans = inf
        def dfs(mat, val):
            nonlocal ans
            if val >= ans: return inf
            found = False
            for i in range(n):
                for j in range(m):
                    if mat[i][j] == 0:
                        found = True
                        break
                if found: break
            if not found:
                return 0
            finish = False
            e = 0
            for e in range(1, min(m, n)):
                if i + e == n or j + e == m:
                    e -= 1
                    break
                for u in range(e + 1):
                    if mat[i + u][j + e] == 1:
                        e -= 1
                        finish = True
                        break
                    if mat[i + e][j + u] == 1:
                        e -= 1
                        finish = True
                        break
                if finish: break
            # e + 1 表示 以[i, j]为左上角，最大的正方形边长
            for u in range(e + 1):
                for v in range(e + 1):
                    mat[i + u][j + v] = 1
            res = inf
            for u in range(e, -1, -1):
                aa = dfs(mat, val + 1)
                res = min(res, aa)
                for v in range(u + 1):
                    mat[i + v][j + u] = 0
                    mat[i + u][j + v] = 0
                ans = min(ans, val + 1 + res)
            return res + 1

        dfs([[0] * m for _ in range(n)], 0)
        return ans


obj = Solution()
print(obj.tilingRectangle(1, 2))  # 5
print(obj.tilingRectangle(5, 8))  # 5
print(obj.tilingRectangle(11, 13))  # 6
print(obj.tilingRectangle(2, 3))  # 3

