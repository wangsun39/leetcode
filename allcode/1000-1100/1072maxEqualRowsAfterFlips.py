# 给定 m x n 矩阵 matrix 。
#
# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
#
# 返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。
#
#
#
# 示例 1：
#
# 输入：matrix = [[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
# 示例 2：
#
# 输入：matrix = [[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
# 示例 3：
#
# 输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] == 0 或 1
from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxEqualRowsAfterFlips1(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        n_group = 1
        group = [range(r)]
        def divide(l, j):   # l 是一个分组的所有下标列表，第 j 列与第 0 列 对应行进行异或运算，按结果进行分组
            a, b = [], []
            for i in l:
                if matrix[i][0] ^ matrix[i][j]:
                    a.append(i)
                else:
                    b.append(i)
            if len(a) > len(b):
                return a, b
            return b, a
        for i in range(1, c):
            for k, g in enumerate(group):
                if len(g) == 0: continue
                a, b = divide(g, i)
                if len(b) == 0: continue
                group[k] = a
                group.append(b)
        return max(len(g) for g in group)

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 更简洁的方法
        r, c = len(matrix), len(matrix[0])
        nums = [0] * r
        for i in range(r):
            reverse = True if matrix[i][0] == 1 else False
            for j in range(c):
                if reverse:
                    matrix[i][j] ^= 1
                nums[i] = (nums[i] << 1) + matrix[i][j]
        c = Counter(nums)
        return max(c.values())

