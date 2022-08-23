# 一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
#
# 返回 将这个矩阵变为  “棋盘”  所需的最小移动次数 。如果不存在可行的变换，输出 -1。
#
# “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
#
#  
#
# 示例 1:
#
#
#
# 输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# 输出: 2
# 解释:一种可行的变换方式如下，从左到右：
# 第一次移动交换了第一列和第二列。
# 第二次移动交换了第二行和第三行。
# 示例 2:
#
#
#
# 输入: board = [[0, 1], [1, 0]]
# 输出: 0
# 解释: 注意左上角的格值为0时也是合法的棋盘，也是合法的棋盘.
# 示例 3:
#
#
#
# 输入: board = [[1, 0], [1, 0]]
# 输出: -1
# 解释: 任意的变换都不能使这个输入变为合法的棋盘。
#  
#
# 提示：
#
# n == board.length
# n == board[i].length
# 2 <= n <= 30
# board[i][j] 将只包含 0或 1

from typing import List
from collections import Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        rows = [tuple(e) for e in board]
        cols = []
        for i in range(n):
            cols.append(tuple(board[j][i] for j in range(n)))
        def check(tuples):
            counter = Counter(tuples)
            if len(counter) != 2:
                return False
            v = list(counter.values())
            if abs(v[0] - v[1]) > 1:
                return False
            k = list(counter.keys())
            return abs(k[0].count(1) - k[0].count(0)) <= 1 and abs(k[1].count(1) - k[1].count(0)) <= 1
        if not check(rows) or not check(cols):
            return -1
        def calc(t: tuple):
            c1, c2 = [1, t.count(1)], [0, t.count(0)]
            if c1[1] < c2[1]:
                c1, c2 = c2, c1
            n1 = 0
            for i, e in enumerate(t):
                if i % 2 == 0 and c1[0] != e:
                    n1 += 1
            if n % 2 == 1:
                return n1
            return min(n1, n // 2 - n1)
        return calc(rows[0]) + calc(cols[0])

so = Solution()
print(so.movesToChessboard([[0,1],[1,1]]))  # -1
print(so.movesToChessboard([[1,1,0],[0,0,1],[0,0,1]]))  # 2
print(so.movesToChessboard([[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,1]]))  # 1
print(so.movesToChessboard([[0, 1], [1, 0]])) # 0
print(so.movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]))  # 2
print(so.movesToChessboard([[1, 0], [1, 0]]))  # -1

