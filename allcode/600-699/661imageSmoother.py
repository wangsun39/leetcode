# 图像平滑器 是大小为3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
#
# 每个单元格的 平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
#
# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
#
#
#
# 给你一个表示图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像。
#
# 
#
# 示例 1:
#
#
#
# 输入:img = [[1,1,1],[1,0,1],[1,1,1]]
# 输出:[[0, 0, 0],[0, 0, 0], [0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 示例 2:
#
#
# 输入: img = [[100,200,100],[200,50,200],[100,200,100]]
# 输出: [[137,141,137],[141,138,141],[137,141,137]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
# 对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
# 对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
# 
#
# 提示:
#
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255



from leetcode.allcode.competition.mypackage import *


class Solution:
    def imageSmoother1(self, img: List[List[int]]) -> List[List[int]]:
        N1, N2 = len(img), len(img[0])
        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        corner = [[0,0], [0, N2-1], [N1-1,0], [N1-1,N2-1]]
        avg = [[0 for _ in range(N2)] for _ in range(N1)]
        for i in range(N1):
            for j in range(N2):
                sumA = 0
                for e in dir:
                    if 0 <= i + e[0] < N1 and 0 <= j + e[1] < N2:
                        sumA += img[i + e[0]][j + e[1]]
                if [i, j] in corner:
                    avg[i][j] = sumA // (min(N1, 2) * min(N2, 2))
                elif i in [0, N1-1] or j in [0,N2-1]:
                    avg[i][j] = sumA // (min(N1, N2, 2) * 3)
                else:
                    avg[i][j] = sumA // 9
        return avg

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # 2024/11/18 二维前缀和
        r, c = len(img), len(img[0])
        s = [[0] * (c + 1) for _ in range(r + 1)]
        for i, row in enumerate(img):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        ans = [[0] * c for _ in range(r)]
        for i, j in product(range(r), range(c)):
            # 计算求和区域
            r1, r2 = max(0, i - 1), min(r, i + 2)
            c1, c2 = max(0, j - 1), min(c, j + 2)
            cnt = (r2 - r1) * (c2 - c1)
            ans[i][j] = (s[r2][c2] - s[r1][c2] - s[r2][c1] + s[r1][c1]) // cnt
        return ans

so = Solution()
print(so.imageSmoother([[6,9,7]]))
print(so.imageSmoother([[1]]))
print(so.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
print(so.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))

