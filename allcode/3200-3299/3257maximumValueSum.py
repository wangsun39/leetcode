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
# 3 <= m == board.length <= 500
# 3 <= n == board[i].length <= 500
# -109 <= board[i][j] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        r, c = len(board), len(board[0])
        pre_mx = []  # 前i行的三个最大值及列
        sup_mx = []  # 后i行的三个最大值及列
        cur = [[x, i] for i, x in enumerate(board[0])]  # 记录每列的最大值
        pre_mx.append(deepcopy(sorted(cur, reverse=True)[:3]))
        for i in range(1, r):
            for j in range(c):
                if cur[j][0] < board[i][j]:
                    cur[j][0] = board[i][j]
            pre_mx.append(deepcopy(sorted(cur, reverse=True)[:3]))
        cur = [[x, i] for i, x in enumerate(board[-1])]  # 记录每列的最大值
        sup_mx.append(deepcopy(sorted(cur, reverse=True)[:3]))
        for i in range(r - 2, -1, -1):
            for j in range(c):
                if cur[j][0] < board[i][j]:
                    cur[j][0] = board[i][j]
            sup_mx.append(deepcopy(sorted(cur, reverse=True)[:3][:]))
        # print(pre_mx)
        # print(sup_mx)
        ans = -inf
        for mid in range(1, r - 1):
            # 枚举中间行
            cur = sorted([[x, i] for i, x in enumerate(board[mid])], reverse=True)
            for i in range(3):
                vi, idi = pre_mx[mid - 1][i]
                for j in range(3):
                    vj, idj = cur[j]
                    for k in range(3):
                        vk, idk = sup_mx[r - 1 - (mid + 1)][k]
                        if idi != idj != idk != idi:
                            ans = max(ans, vi + vj + vk)

        return ans


so = Solution()
print(so.maximumValueSum(board = [[1,2,3],[4,5,6],[7,8,9]]))
print(so.maximumValueSum(board = [[-53,-86,-80],[-28,16,-42],[-88,38,-66]]))  # -57
print(so.maximumValueSum(board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]))
print(so.maximumValueSum(board = [[1,1,1],[1,1,1],[1,1,1]]))




