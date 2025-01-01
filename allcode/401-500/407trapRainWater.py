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
        r, c = len(heightMap), len((heightMap[0]))
        ans = 0
        right = [[-1] * c for _ in range(r)]  # [i][j] 右侧第一个比它大的值的列号
        down = [[-1] * c for _ in range(r)]  # [i][j] 下侧第一个比它大的值的行号
        left = [[-1] * c for _ in range(r)]  # [i][j] 左侧第一个比它大的值的列号
        up = [[-1] * c for _ in range(r)]  # [i][j] 上侧第一个比它大的值的行号
        for i in range(r):
            stack = [c - 1]
            for j in range(c - 2, -1, -1):
                while stack and stack[-1] <= heightMap[i][j]:
                    stack.pop(0)
                if stack:
                    right[i][j] = stack[-1]
                stack.append(j)
        for i in range(r):
            stack = [0]
            for j in range(1, c):
                while stack and stack[-1] <= heightMap[i][j]:
                    stack.pop(0)
                if stack:
                    right[i][j] = stack[-1]
                stack.append(j)
        for j in range(c):
            stack = [r - 1]
            for i in range(r - 2, -1, -1):
                while stack and stack[-1] <= heightMap[i][j]:
                    stack.pop(0)
                if stack:
                    down[i][j] = stack[-1]
                stack.append(i)
        for j in range(c):
            stack = [0]
            for i in range(1, r):
                while stack and stack[-1] <= heightMap[i][j]:
                    stack.pop(0)
                if stack:
                    down[i][j] = stack[-1]
                stack.append(i)
        for i in range(r):
            for j in range(c):
                if right[i][j] == -1 or down[i][j] == -1 or left[i][j] == -1 or up[i][j] == -1: continue
                ans += (right[i][j] - j) + (down[i][j] - i) - 1
        return ans

so = Solution()
print(so.trapRainWater(heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
print(so.trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))




