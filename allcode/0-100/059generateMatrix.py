# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 示例 2：
#
# 输入：n = 1
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= n <= 20

from leetcode.allcode.competition.mypackage import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_d = 0
        x = y = 0
        for i in range(n * n):
            ans[x][y] = i + 1
            x0, y0 = dir[cur_d]
            u, v = x + x0, y + y0
            if 0 <= u < n and 0 <= v < n and ans[u][v] == 0:
                pass
            else:
                cur_d = (cur_d + 1) % 4
                x0, y0 = dir[cur_d]
                u, v = x + x0, y + y0
            x, y = u, v
        return ans

so = Solution()
print(so.generateMatrix(3))
print(so.generateMatrix(1))




