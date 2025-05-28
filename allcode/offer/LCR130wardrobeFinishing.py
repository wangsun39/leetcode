# 家居整理师将待整理衣橱划分为 m x n 的二维矩阵 grid，其中 grid[i][j] 代表一个需要整理的格子。整理师自 grid[0][0] 开始 逐行逐列 地整理每个格子。
#
# 整理规则为：在整理过程中，可以选择 向右移动一格 或 向下移动一格，但不能移动到衣柜之外。同时，不需要整理 digit(i) + digit(j) > cnt 的格子，其中 digit(x) 表示数字 x 的各数位之和。
#
# 请返回整理师 总共需要整理多少个格子。
#
#
#
# 示例 1：
#
# 输入：m = 4, n = 7, cnt = 5
# 输出：18
#
#
# 提示：
#
# 1 <= n, m <= 100
# 0 <= cnt <= 20

from leetcode.allcode.competition.mypackage import *

class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        def count(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
        for i in range(m):
            ci = count(i)
            for j in range(n):
                cj = count(j)
                if ci + cj


so = Solution()
print(so.wardrobeFinishing(grid = [["a","a"]], target = "aaa"))




