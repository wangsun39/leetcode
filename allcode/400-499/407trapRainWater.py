# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
#
#
# 示例 1:
#
#
#
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
# 示例 2:
#
#
#
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#
#
# 提示:
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(heightMap), len((heightMap[0]))
        if r == 1 or c == 1: return 0
        mx_high = [[-1] * c for _ in range(r)]  # 每个位置最终的最大高度
        ans = 0
        hp = []
        for i in range(r):
            for j in [0, c - 1]:
                heappush(hp, [heightMap[i][j], i, j])
                mx_high[i][j] = heightMap[i][j]
        for j in range(1, c - 1):
            for i in [0, r - 1]:
                heappush(hp, [heightMap[i][j], i, j])
                mx_high[i][j] = heightMap[i][j]
        while hp:
            h, x, y = heappop(hp)
            for x0, y0 in dir:
                u, v = x + x0, y + y0
                if 0 < u < r - 1 and 0 < v < c - 1 and mx_high[u][v] == -1:
                    mx_high[u][v] = max(heightMap[u][v], h)
                    ans += mx_high[u][v] - heightMap[u][v]
                    heappush(hp, [mx_high[u][v], u, v])
        return ans


so = Solution()
print(so.trapRainWater(heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
print(so.trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))




