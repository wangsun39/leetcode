# 给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。
#
# 返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。
#
# 示例 1：
#
# 输入：
# [
#    [1,0,1],
#    [0,0,1],
#    [0,0,1]
# ]
# 输出：[1,0,2]
# 解释：输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
# 示例 2：
#
# 输入：
# [
#    [0,1,1],
#    [1,0,1],
#    [1,1,0]
# ]
# 输出：[0,0,1]
# 提示：
#
# matrix.length == matrix[0].length <= 200

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        s1 = [[0] * (c + 1) for _ in range(r)]  # 横向前缀和
        for i in range(r):
            for j in range(1, c + 1):
                s1[i][j] = s1[i][j - 1] + matrix[i][j - 1]
        s2 = [[0] * c for _ in range(r + 1)]  # 纵向前缀和
        for i in range(1, r + 1):
            for j in range(c):
                s2[i][j] = s2[i - 1][j] + matrix[i - 1][j]
        mx = 0
        x = y = -1
        m = min(r, c)
        for i in range(r):
            for j in range(c):
                for k in range(mx, m):  # 边长为k+1
                    if i + k >= r or j + k >= c: break
                    u, v = i + k, j + k
                    # 左下 [u, j], 右上 [i, v], 右下 [u, v]
                    # print(s2[u + 1][j], s2[i][j], s2[u + 1][v], s2[i][v])
                    if s2[u + 1][j] - s2[i][j] or s1[i][v + 1] - s1[i][j]: break
                    if s2[u + 1][v] - s2[i][v] or s1[u][v + 1] - s1[u][j]: continue
                    if k + 1 > mx:
                        x, y = i, j
                        mx = k + 1
                    elif k + 1 == mx:
                        [x, y] = min([x, y], [i, j])
                    else:
                        break
        if mx == 0:
            return []
        return [x, y, mx]


so = Solution()
print(so.findSquare([[1, 1, 1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]))
print(so.findSquare([
   [1,0,1],
   [0,0,1],
   [0,0,1]
]))





