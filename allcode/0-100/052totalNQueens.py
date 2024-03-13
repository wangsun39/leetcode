# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
# 提示：
#
# 1 <= n <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        def dfs(choose):
            nonlocal ans
            if len(choose) == n:
                ans += 1
                return
            row = len(choose)
            col = set(y for _, y in choose)
            for j in range(n):
                if j in col: continue
                found = True
                for x, y in choose:
                    if abs(y - j) == abs(x - row):
                        found = False
                        break
                if found:
                    dfs(choose + [[row, j]])
        dfs([])
        return ans

so = Solution()
print(so.totalNQueens(9))
print(so.totalNQueens(4))
print(so.totalNQueens(1))




