# 给你两个图像 img1 和 img2 ，两个图像的大小都是 n x n ，用大小相同的二进制正方形矩阵表示。二进制矩阵仅由若干 0 和若干 1 组成。
#
# 转换 其中一个图像，将所有的 1 向左，右，上，或下滑动任何数量的单位；然后把它放在另一个图像的上面。该转换的 重叠 是指两个图像 都 具有 1 的位置的数目。
#
# 请注意，转换 不包括 向任何方向旋转。越过矩阵边界的 1 都将被清除。
#
# 最大可能的重叠数量是多少？
#
#
#
# 示例 1：
#
#
# 输入：img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# 输出：3
# 解释：将 img1 向右移动 1 个单位，再向下移动 1 个单位。
#
# 两个图像都具有 1 的位置的数目是 3（用红色标识）。
#
# 示例 2：
#
# 输入：img1 = [[1]], img2 = [[1]]
# 输出：1
# 示例 3：
#
# 输入：img1 = [[0]], img2 = [[0]]
# 输出：0
#
#
# 提示：
#
# n == img1.length == img1[i].length
# n == img2.length == img2[i].length
# 1 <= n <= 30
# img1[i][j] 为 0 或 1
# img2[i][j] 为 0 或 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img = [[0] * (n * 3 - 2) for _ in range(n * 3 - 2)]
        for i in range(n - 1, n * 2 - 1):
            for j in range(n - 1, n * 2 - 1):
                img[i][j] = img1[i - (n - 1)][j - (n - 1)]
        ans = 0

        def calc(r, c):
            res = 0
            for i in range(n):
                for j in range(n):
                    res += img[r + i][c + j] == img2[i][j] == 1
            return res
        for i in range(n * 2 - 1):
            for j in range(n * 2 - 1):
                ans = max(ans, calc(i, j))
        return ans



so = Solution()
print(so.largestOverlap(img1 = [[1]], img2 = [[1]]))

