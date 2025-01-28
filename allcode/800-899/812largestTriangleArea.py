# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
# 注意:
#
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在10^-6以内都认为是正确答案。


from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(A, B, C):
            [A, B, C] = sorted([A, B, C], key=lambda x: x[0])
            # print(A, B, C)
            S1 = (A[1] + B[1]) * (abs(A[0] - B[0])) / 2
            S2 = (C[1] + B[1]) * (abs(C[0] - B[0])) / 2
            S3 = (A[1] + C[1]) * (abs(A[0] - C[0])) / 2
            return abs(S1 + S2 - S3)
        # def area(A, B, C):
        #     return (A[0] * (B[1] - C[1]) + B[0] * (B[1] - C[1]) + A[0] * (B[1] - C[1])) / 2
        area(points[0], points[1], points[2])
        n = len(points)
        ans = 0
        for p in points:
            p[0], p[1] = p[0] + 50, p[1] + 50
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, area(points[i], points[j], points[k]))
        return ans



so = Solution()
print(so.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))

