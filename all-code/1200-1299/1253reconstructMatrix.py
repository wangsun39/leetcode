# 给你一个 2 行 n 列的二进制数组：
#
# 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
# 第 0 行的元素之和为 upper。
# 第 1 行的元素之和为 lower。
# 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
# 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
#
# 如果有多个不同的答案，那么任意一个都可以通过本题。
#
# 如果不存在符合要求的答案，就请返回一个空的二维数组。
#
#
#
# 示例 1：
#
# 输入：upper = 2, lower = 1, colsum = [1,1,1]
# 输出：[[1,1,0],[0,0,1]]
# 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
# 示例 2：
#
# 输入：upper = 2, lower = 3, colsum = [2,2,1,1]
# 输出：[]
# 示例 3：
#
# 输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
#
#
# 提示：
#
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2


from typing import List
from collections import Counter
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower: return []
        n = len(colsum)
        ans = [[-1] * n for _ in range(2)]
        cnt = 0
        for i, x in enumerate(colsum):
            if x == 2:
                ans[0][i] = ans[1][i] = 1
                cnt += 1
            elif x == 0:
                ans[0][i] = ans[1][i] = 0
        if cnt > min(upper, lower): return []
        for i in range(n):
            if ans[0][i] != -1: continue
            if cnt < upper:
                cnt += 1
                ans[0][i] = 1
                ans[1][i] = 0
            else:
                ans[0][i] = 0
                ans[1][i] = 1
        return ans



obj = Solution()
print(obj.reconstructMatrix(upper = 9, lower = 2, colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2]))
print(obj.reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
print(obj.reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
print(obj.reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))

