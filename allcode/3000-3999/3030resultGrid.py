# 给你一个下标从 0 开始、大小为 m x n 的网格 image ，表示一个灰度图像，其中 image[i][j] 表示在范围 [0..255] 内的某个像素强度。另给你一个 非负 整数 threshold 。
#
# 如果 image[a][b] 和 image[c][d] 满足 |a - c| + |b - d| == 1 ，则称这两个像素是 相邻像素 。
#
# 区域 是一个 3 x 3 的子网格，且满足区域中任意两个 相邻 像素之间，像素强度的 绝对差 小于或等于 threshold 。
#
# 区域 内的所有像素都认为属于该区域，而一个像素 可以 属于 多个 区域。
#
# 你需要计算一个下标从 0 开始、大小为 m x n 的网格 result ，其中 result[i][j] 是 image[i][j] 所属区域的 平均 强度，向下取整 到最接近的整数。如果 image[i][j] 属于多个区域，result[i][j] 是这些区域的 “取整后的平均强度” 的 平均值，也 向下取整 到最接近的整数。如果 image[i][j] 不属于任何区域，则 result[i][j] 等于 image[i][j] 。
#
# 返回网格 result 。
#
#
#
# 示例 1：
#
#
# 输入：image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3
# 输出：[[9,9,9,9],[9,9,9,9],[9,9,9,9]]
# 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 9 ，而第二个区域的平均强度为 9.67 ，向下取整为 9 。两个区域的平均强度为 (9 + 9) / 2 = 9 。由于所有像素都属于区域 1 、区域 2 或两者，因此 result 中每个像素的强度都为 9 。
# 注意，在计算多个区域的平均值时使用了向下取整的值，因此使用区域 2 的平均强度 9 来进行计算，而不是 9.67 。
# 示例 2：
#
#
# 输入：image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12
# 输出：[[25,25,25],[27,27,27],[27,27,27],[30,30,30]]
# 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 25 ，而第二个区域的平均强度为 30 。两个区域的平均强度为 (25 + 30) / 2 = 27.5 ，向下取整为 27 。图像中第 0 行的所有像素属于区域 1 ，因此 result 中第 0 行的所有像素为 25 。同理，result 中第 3 行的所有像素为 30 。图像中第 1 行和第 2 行的像素属于区域 1 和区域 2 ，因此它们在 result 中的值为 27 。
# 示例 3：
#
# 输入：image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1
# 输出：[[5,6,7],[8,9,10],[11,12,13]]
# 解释：图像中不存在任何区域，因此对于所有像素，result[i][j] == image[i][j] 。
#
#
# 提示：
#
# 3 <= n, m <= 500
# 0 <= image[i][j] <= 255
# 0 <= threshold <= 255

from leetcode.allcode.competition.mypackage import *

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(image), len(image[0])
        region = [[inf] * c for _ in range(r)]  # 以[i,j]为中心的区域平均强度

        def check(i, j):
            for ii in range(-1, 2, 1):
                for jj in range(-1, 2, 1):
                    u, v = i + ii, j + jj
                    for x0, y0 in dir:
                        x, y = x0 + u, y0 + v
                        if i - 1 <= x <= i + 1 and j - 1 <= y <= j + 1 and abs(image[x][y] - image[u][v]) > threshold:
                            return False
            return True

        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if check(i, j):
                    s = 0
                    for ii in range(-1, 2, 1):
                        for jj in range(-1, 2, 1):
                            s += image[i + ii][j + jj]
                    region[i][j] = s // 9

        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                s = cnt = 0
                for ii in range(-1, 2, 1):
                    for jj in range(-1, 2, 1):
                        u, v = i + ii, j + jj
                        if 0 <= u < r and 0 <= v < c and region[u][v] != inf:
                            s += region[i + ii][j + jj]
                            cnt += 1
                if cnt:
                    ans[i][j] = s // cnt
                else:
                    ans[i][j] = image[i][j]
        return ans




so = Solution()
print(so.resultGrid([[1,1,4,1],[10,8,13,17],[2,12,1,16]], 14))
print(so.resultGrid(image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3))
print(so.resultGrid(image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12))
print(so.resultGrid(image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1))




