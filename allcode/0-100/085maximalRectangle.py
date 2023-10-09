# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 示例 2：
#
# 输入：matrix = []
# 输出：0
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
# 示例 4：
#
# 输入：matrix = [["1"]]
# 输出：1
# 示例 5：
#
# 输入：matrix = [["0","0"]]
# 输出：0
#  
#
# 提示：
#
# rows == matrix.length
# cols == matrix[0].length
# 0 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'




from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(lengths: List[int]) -> int: # 用84题的方法计算
            lengths.append(0)
            N = len(lengths)
            stack = [[-1, 0]]  # 第一个表示下标，第二个表示heights中对应的元素
            largest = [0] * N
            for i in range(N):
                while stack[-1][1] > lengths[i]:
                    last_key, last_value = stack.pop()
                    largest[last_key] = (i - stack[-1][0] - 1) * last_value
                stack.append([i, lengths[i]])
            return max(largest)

        row = len(matrix)
        if row <= 0:
            return 0
        column = len(matrix[0])
        lengths, res = [0] * column, 0
        for i in range(row):   # 将每行想象为一个柱状图，柱子的高度为从当前行的对应每个元素向上的连续 '1' 个数，每行依次调用 84 题的解法
            for j in range(column):
                lengths[j] = lengths[j] + 1 if '1' == matrix[i][j] else 0
            res = max(res, largestRectangleArea(lengths))
        return res


so = Solution()
print(so.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(so.maximalRectangle([["0","0"]]))
print(so.maximalRectangle([["1"]]))

