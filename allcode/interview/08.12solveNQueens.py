# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
#
# 注意：本题相对原题做了扩展
#
# 示例：
#
#  输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释：4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

from leetcode.allcode.competition.mypackage import *

class Solution:
    def solveNQueens1(self, n: int) -> List[List[str]]:

        def dfs(row, vis1, diag1, diag2):  # vis1表示已经用过的列，diag1, diag2 分别表示哪些左右对角线已被占用
            res = []
            if row == n: return [[]]
            for i in range(n):
                if vis1 & (1 << i): continue
                if i - row in diag1 or i + row in diag2: continue
                v = dfs(row + 1, vis1 | (1 << i), diag1 + [i - row], diag2 + [i + row])
                cur = '.' * i + 'Q' + '.' * (n - i - 1)
                for lines in v:
                    res.append([cur] + lines)
            return res

        return dfs(0, 0, [], [])

    def solveNQueens(self, n: int) -> List[List[str]]:
        @cache
        def dfs(row, vis1, diag1, diag2):  # vis1表示已经用过的列，diag1, diag2 分别表示哪些左右对角线已被占用
            res = []
            if row == n: return [[]]
            for i in range(n):
                if vis1 & (1 << i): continue
                if diag1 & (1 << (i - row + n)) or diag2 & (1 << (i + row)): continue
                v = dfs(row + 1, vis1 | (1 << i), diag1 | (1 << (i - row + n)), diag2 | (1 << (i + row)))
                cur = '.' * i + 'Q' + '.' * (n - i - 1)
                for lines in v:
                    res.append([cur] + lines)
            return res

        return dfs(0, 0, 0, 0)


so = Solution()
print(so.solveNQueens(4))




