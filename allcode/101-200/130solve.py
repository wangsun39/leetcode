# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
#
# 示例 1：
#
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
# 提示：
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        flag = set()
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(x, y):
            if (x, y) in flag:
                return
            flag.add((x, y))
            for u, v in dir:
                if 0 <= x + u < r and 0 <= y + v < c:
                    if board[x + u][y + v] == 'O':
                        dfs(x + u, y + v)
        for i in range(c):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[r - 1][i] == 'O':
                dfs(r - 1, i)
        for j in range(r):
            if board[j][0] == 'O':
                dfs(j, 0)
            if board[j][c - 1] == 'O':
                dfs(j, c - 1)
        for i in range(r):
            for j in range(c):
                if (i, j) not in flag and board[i][j] == 'O':
                    board[i][j] = 'X'
        print(board)



so = Solution()
print(so.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))


