# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
#
# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。
#
# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。
#
# 返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。
#
#  
#
# 示例 1：
#
#
#
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# 示例 2：
#
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
#  
#
# 提示：
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        M = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            M[i][0] |= 1
            M[i][col - 1] |= 2
        for j in range(col):
            M[0][j] |= 1
            M[row - 1][j] |= 2
        # print(M)

        def update():
            res = False
            for i in range(row):
                for j in range(col - 1, -1, -1):
                    old = M[i][j]
                    if j + 1 < col and heights[i][j] >= heights[i][j + 1]:
                        M[i][j] |= M[i][j + 1]
                    if i - 1 >= 0 and heights[i][j] >= heights[i - 1][j]:
                        M[i][j] |= M[i - 1][j]
                    if old != M[i][j]:
                        res = True
            for i in range(row - 1, -1, -1):
                for j in range(col):
                    old = M[i][j]
                    if j - 1 >= 0 and heights[i][j] >= heights[i][j - 1]:
                        M[i][j] |= M[i][j - 1]
                    if i + 1 < row and heights[i][j] >= heights[i + 1][j]:
                        M[i][j] |= M[i + 1][j]
                    if old != M[i][j]:
                        res = True
            return res
        while update():
            # print(M)
            pass
        ans = []
        for i in range(row):
            for j in range(col):
                if M[i][j] == 3:
                    ans.append([i, j])
        return ans





so = Solution()

