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
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        @cache
        def count(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
        vis = {(0, 0)}
        dq1 = deque([(0,0)])
        while dq1:
            dq2 = deque()
            while dq1:
                x, y = dq1.popleft()
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < m and 0 <= v < n and (u, v) not in vis and count(u) + count(v) <= cnt:
                        dq2.append((u, v))
                        vis.add((u, v))
            dq1 = dq2

        return len(vis)


so = Solution()
print(so.wardrobeFinishing(m = 3, n = 1, cnt = 0))
print(so.wardrobeFinishing(m = 16, n = 8, cnt = 4))
print(so.wardrobeFinishing(m = 4, n = 7, cnt = 5))




