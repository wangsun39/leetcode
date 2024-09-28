# 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
#
#
#
# 示例 1：
#
#
#
# 输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
# 示例 2：
#
#
#
# 输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
#
#
#
# 提示：
#
# 1 <= m, n <= 150
# mat[i][j] 仅包含 0 或 1


from leetcode.allcode.competition.mypackage import *

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        right = [[0] * c for _ in range(r)]  # 记录每个位置及后侧有多少个连续1
        for i in range(r):
            stack = []
            for j in range(c + 1):
                if j < c and mat[i][j] == 1:
                    stack.append(j)
                else:
                    while stack:
                        k = stack.pop()
                        right[i][k] = j - k
        # print(right)
        ans = 0
        for i in range(r):
            for j in range(c):
                max_width = right[i][j]
                for k in range(i, r):
                    max_width = min(max_width, right[k][j])
                    if max_width == 0: break
                    ans += max_width
        return ans







so = Solution()
print(so.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
print(so.numSubmat(mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]))





