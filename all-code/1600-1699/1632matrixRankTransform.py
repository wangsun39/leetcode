# 给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的秩。
#
# 每个元素的 秩 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：
#
# 秩是从 1 开始的一个整数。
# 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么：
# 如果 p < q ，那么 rank(p) < rank(q)
# 如果 p == q ，那么 rank(p) == rank(q)
# 如果 p > q ，那么 rank(p) > rank(q)
# 秩 需要越 小 越好。
# 题目保证按照上面规则 answer 数组是唯一的。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2],[3,4]]
# 输出：[[1,2],[2,3]]
# 解释：
# matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
# matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。
# 示例 2：
#
#
# 输入：matrix = [[7,7],[7,7]]
# 输出：[[1,1],[1,1]]
# 示例 3：
#
#
# 输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# 输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# 示例 4：
#
#
# 输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
# 输出：[[5,1,4],[1,2,3],[6,3,1]]
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -109 <= matrix[row][col] <= 109




from typing import Optional,List
from collections import defaultdict
from heapq import *
from math import *


# Definition for a binary tree node.
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        ans = [[0] * col for _ in range(row)]
        row_val, col_val = [-inf] * row, [-inf] * col  # 根据已计算出秩的元素，对应的矩阵行列的元素最大值
        row_rank, col_rank = [1] * row, [1] * col

        def proc(val, s): # list s 中的点在matrix中的值都相同，并且这些点都在一个并查集中
            mx_rank = 0
            for ss in s:
                x, y = ss // col, ss % col
                mx_rank = max(mx_rank, row_rank[x], col_rank[y])
                if row_val[x] != -inf and row_val[x] < val:
                    mx_rank = max(mx_rank, row_rank[x] + 1)
                if col_val[y] != -inf and col_val[y] < val:
                    mx_rank = max(mx_rank, col_rank[y] + 1)

            for ss in s:
                x, y = ss // col, ss % col
                row_rank[x] = col_rank[y] = mx_rank
                row_val[x] = col_val[y] = val
                ans[x][y] = mx_rank

        fa = list(range(row * col))
        def find(x):
            # print(x)
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(row):
            dd = defaultdict(list)
            for j in range(col):
                if matrix[i][j] in dd:
                    union(dd[matrix[i][j]][0], i * col + j)
                dd[matrix[i][j]].append(i * col + j)
        for j in range(col):
            dd = defaultdict(list)
            for i in range(row):
                if matrix[i][j] in dd:
                    union(dd[matrix[i][j]][0], i * col + j)
                dd[matrix[i][j]].append(i * col + j)
        d = defaultdict(list)
        for i in range(row * col):
            x = find(i)  # i的fa的行列坐标值
            e = matrix[x // col][x % col]
            d[(e, x)].append(i)

        l = [[k[0], v] for k, v in d.items()]
        l.sort()

        for k, ll in l:
            proc(k, ll)

        return ans

so = Solution()

print(so.matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]))
print(so.matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
print(so.matrixRankTransform([[1,2],[3,4]]))
print(so.matrixRankTransform([[7,7],[7,7]]))
print(so.matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]))




