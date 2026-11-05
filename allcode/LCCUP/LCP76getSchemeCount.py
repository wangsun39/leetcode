# 在大小为 n * m 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣：
#
# 两颗异色棋子在同一行或者同一列
# 两颗异色棋子之间恰好只有一颗棋子
# 注：异色棋子之间可以有空位
#
# 由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。chessboard[i][j] 表示棋盘第 i 行 j 列的状态：
#
# 若为 . ，表示当前格子确定为空
# 若为 B ，表示当前格子确定为 黑棋
# 若为 R ，表示当前格子确定为 红棋
# 若为 ? ，表示当前格子待定
# 现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 无法 产生共鸣。请返回可以满足上述条件的放置方案数量。
#
# 示例1：
#
# 输入：n = 3, m = 3, chessboard = ["..R","..B","?R?"]
#
# 输出：5
#
# 解释：给定的棋盘如图：image.png{:height=150px} 所有符合题意的最终局面如图：image.png
#
# 示例2：
#
# 输入：n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]
#
# 输出：105
#
# 提示：
#
# n == chessboard.length
# m == chessboard[i].length
# 1 <= n*m <= 30
# chessboard 中仅包含 "."、"B"、"R"、"?"

from leetcode.allcode.competition.mypackage import *

# 定义7种状态
X, R, B, R2, B2, RB, BR = 0, 1, 2, 3, 4, 5, 6

T = [[-1] * 7 for _ in range(7)]  # 状态迁移表
for i in range(7): T[i][0] = i  # 任何状态遇到空，
# 固定的状态转移
T[X][R] = R
T[X][B] = B
T[R][R] = R2
T[R][B] = RB
T[B][R] = BR
T[B][B] = B2
T[R2][R] = R2
T[B2][B] = B2
T[RB][R] = BR
T[BR][B] = RB

pow7 = [7 ** j for j in range(6)]

class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        if n < m:
            # 转置
            chessboard = list(zip(*chessboard))
            n, m = m, n

        N = 7 ** m  # 所有可能的m列的状态组合总数

        # 当前考虑第 i 行；当前考虑第 j 列；当前的所有列的状态表示为 col_states，为 7 进制数，每个数位为各个列的状态；当前行的状态为 row_state。
        # dp[i][j][col_states][row_state]
        dp = [[[[0] * 7 for _ in range(N)] for _ in range(m)] for _ in range(n + 1)]  # 第一个维度多留一行，作为哨兵方便统一处理
        dp[0][0][0][0] = 1
        for i in range(n):
            for j in range(m):
                # 从做到右，从上到下，一个个格子遍历，用前一个格子的状态更新下个格子的状态
                ni, nj = i, j + 1  # 下个格子的位置
                if nj == m:  # 换行
                    ni, nj = i + 1, 0
                xp = -1  # 当前格子期望的值， -1 表示 ?
                if chessboard[i][j] == 'R': xp = R
                elif chessboard[i][j] == 'B': xp = B
                elif chessboard[i][j] == '.': xp = 0

                # pos = 7 ** j  # 第j列，在 col_states 中的位置
                base = pow7[j]
                for h in range(N):  # 枚举每种 m 列的组合
                    st = h // base
                    st = st % 7  # 取当前列的状态， 从7进制数角度考虑，取出第j位
                    for c in range(7):  # 枚举当前行的状态
                        if dp[i][j][h][c] == 0: continue   # 这步优化，至关重要
                        if xp != -1:
                            if T[st][xp] != -1 and T[c][xp] != -1:
                                nh = h + (T[st][xp] - st) * base
                                nc = T[c][xp]
                                if ni != i:
                                    nc = 0  # 下个格子跨行了
                                # print(ni,nj,nh,nc,N)
                                dp[ni][nj][nh][nc] += dp[i][j][h][c]
                            continue
                        for ne in range(3):  #
                            if T[st][ne] != -1 and T[c][ne] != -1:
                                # 列的状态 + 当前格子颜色 能匹配到一个合理的下个状态
                                # 行的状态 + 当前格子颜色
                                # T[st][ne] 更新到 h 中对应的7进制数的数位里面
                                nh = h + (T[st][ne] - st) * base
                                nc = T[c][ne]
                                if ni != i:
                                    nc = 0  # 下个格子跨行了
                                # print(ni,nj,nh,nc,N)
                                dp[ni][nj][nh][nc] += dp[i][j][h][c]

        ans = sum(dp[n][0][i][0] for i in range(N))
        return ans


so = Solution()
print(so.getSchemeCount(n = 3, m = 3, chessboard = ["..R","..B","?R?"]))




