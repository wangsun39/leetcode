# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为11（即，2+3+5+1= 11）。
# 示例 2：
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
# 提示：
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
#
#
# 进阶：
#
# 你可以只使用 O(n)的额外空间（n 为三角形的总行数）来解决这个问题吗？



from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        last, current = [0] * N, [0] * N
        last[0] = triangle[0][0]
        for i in range(1, N):
            current[0] = last[0] + triangle[i][0]
            current[i] = last[i - 1] + triangle[i][i]
            for j in range(1, i):
                current[j] = min(last[j - 1], last[j]) + triangle[i][j]
            # print(last, current)
            last, current = current, last
        return min(last)

so = Solution()
print(so.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(so.minimumTotal([[-10]]))

