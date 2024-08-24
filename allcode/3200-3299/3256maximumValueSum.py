# 给你一个 m x n 的二维整数数组 board ，它表示一个国际象棋棋盘，其中 board[i][j] 表示格子 (i, j) 的 价值 。
#
# 处于 同一行 或者 同一列 车会互相 攻击 。你需要在棋盘上放三个车，确保它们两两之间都 无法互相攻击 。
#
# 请你返回满足上述条件下，三个车所在格子 值 之和 最大 为多少。
#
#
#
# 示例 1：
#
# 输入：board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
#
# 输出：4
#
# 解释：
#
#
#
# 我们可以将车分别放在格子 (0, 2) ，(1, 3) 和 (2, 1) 处，价值之和为 1 + 1 + 2 = 4 。
#
# 示例 2：
#
# 输入：board = [[1,2,3],[4,5,6],[7,8,9]]
#
# 输出：15
#
# 解释：
#
# 我们可以将车分别放在格子 (0, 0) ，(1, 1) 和 (2, 2) 处，价值之和为 1 + 5 + 9 = 15 。
#
# 示例 3：
#
# 输入：board = [[1,1,1],[1,1,1],[1,1,1]]
#
# 输出：3
#
# 解释：
#
# 我们可以将车分别放在格子 (0, 2) ，(1, 1) 和 (2, 0) 处，价值之和为 1 + 1 + 1 = 3 。
#
#
#
# 提示：
#
# 3 <= m == board.length <= 100
# 3 <= n == board[i].length <= 100
# -109 <= board[i][j] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        r, c = len(board), len(board[0])
        r_mx = []  # 记录每行最大的两个数，及其位置
        for i in range(r):
            rr = [[v, j] for j, v in enumerate(board[i])]
            rr.sort(reverse=True)
            r_mx.append([[rr[0][0], rr[0][1]]])
            r_mx[-1].append([rr[1][0], rr[1][1]])
            r_mx[-1].append([rr[2][0], rr[2][1]])

        ans = -inf
        for i in range(r):
            for ii in range(3):
                for j in range(i + 1, r):
                    for jj in range(3):
                        if r_mx[i][ii][1] == r_mx[j][jj][1]: continue
                        for k in range(j + 1, r):
                            for kk in range(3):
                                if r_mx[i][ii][1] == r_mx[k][kk][1] or r_mx[k][kk][1] == r_mx[j][jj][1]: continue
                                ans = max(ans, r_mx[i][ii][0] + r_mx[j][jj][0] + r_mx[k][kk][0])

        return ans


so = Solution()
print(so.maximumValueSum(board = [[1,2,3],[4,5,6],[7,8,9]]))
print(so.maximumValueSum(board = [[-53,-86,-80],[-28,16,-42],[-88,38,-66]]))  # -57
print(so.maximumValueSum(board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]))
print(so.maximumValueSum(board = [[1,1,1],[1,1,1],[1,1,1]]))




