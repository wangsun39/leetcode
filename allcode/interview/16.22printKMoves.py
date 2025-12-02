# 一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。
#
# (1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
# (2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。
#
# 编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。
#
# 网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R', 'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。
#
# 示例 1：
#
# 输入：0
# 输出：["R"]
# 示例 2：
#
# 输入：2
# 输出：
# [
#   "_X",
#   "LX"
# ]
# 示例 3：
#
# 输入：5
# 输出：
# [
#   "_U",
#   "X_",
#   "XX"
# ]
# 说明：
#
# K <= 100000

from leetcode.allcode.competition.mypackage import *


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        cur = (0, 0)
        dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        D = ['R', 'D', 'L', 'U']
        pos = 0
        vis = defaultdict(int)
        vis[(0, 0)] = 0
        x0 = x1 = y0 = y1 = 0
        for _ in range(K):
            if vis[cur] == 0:
                pos += 1
                pos %= 4
            else:
                pos -= 1
                pos %= 4
            now = (cur[0] + dir[pos][0], cur[1] + dir[pos][1])
            vis[cur] ^= 1
            cur = now
            x0 = min(x0, now[0])
            x1 = max(x1, now[0])
            y0 = min(y0, now[1])
            y1 = max(y1, now[1])
        res = []
        for j in range(y1, y0 - 1, -1):
            row = [''] * (x1 - x0 + 1)
            for i in range(x0, x1 + 1):
                row[i - x0] = 'X' if vis[(i, j)] else '_'
            res.append(row)
        res[y0 - cur[1] - 1][cur[0] - x0] = D[pos]
        ans = []
        for line in res:
            ans.append(''.join(line))
        return ans



so = Solution()
print(so.printKMoves(20000))
print(so.printKMoves(0))





