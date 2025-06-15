# 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。
#
#
#
# 输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。
#
# 输出：一个整数，代表最多能在棋盘上放的骨牌数。
#
#
#
# 示例 1：
#
# 输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
# 输出：2
# 解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）
#
#
#
#
# 示例 2：
#
# 输入：n = 3, m = 3, broken = []
# 输出：4
# 解释：下图是其中一种可行的摆放方式
#
#
#
#
# 限制：
#
# 1 <= n <= 8
# 1 <= m <= 8
# 0 <= b <= n * m

from leetcode.allcode.competition.mypackage import *

class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        arr = [[0] * m for _ in range(n)]
        for x, y in broken:
            arr[x][y] = 1

        def dfs(r, c):
            # print(r, c)
            res = 0
            if r == n and c == m: return 0
            for i in range(r, n):
                start = 0
                if i == r:
                    start = c
                for j in range(start, m):
                    if arr[i][j] == 1: continue
                    # 不选 arr[i][j]
                    arr[i][j] = 1
                    res = max(res, dfs(i, j + 1))
                    arr[i][j] = 0
                    # flg = 0
                    # 选 arr[i][j]
                    if j < m - 1 and arr[i][j + 1] == 0:
                        arr[i][j] = arr[i][j + 1] = 1
                        res = max(res, dfs(i, j + 2) + 1)
                        arr[i][j] = arr[i][j + 1] = 0
                        # flg = 1
                    if i < n - 1 and arr[i + 1][j] == 0:
                        arr[i][j] = arr[i + 1][j] = 1
                        res = max(res, dfs(i, j + 1) + 1)
                        arr[i][j] = arr[i + 1][j] = 0
                        flg = 1
                    # if flg == 1:
                    #     break
                    break
            return res

        return dfs(0, 0)

so = Solution()
print(so.domino(n = 8, m = 8, broken = []))
print(so.domino(n = 2, m = 3, broken = [[1, 0], [1, 1]]))




