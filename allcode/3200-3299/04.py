

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        def generate_pascal_triangle(n):  # 杨辉三角
            triangle = []
            for i in range(n):
                row = [None for _ in range(i + 1)]
                row[0], row[-1] = 1, 1
                if i > 1:
                    for j in range(1, len(row) - 1):
                        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                triangle.append(row)
            return triangle

        triangle = generate_pascal_triangle(n)
        # print(triangle)

        orv = [[0] * n for _ in range(n)]  # 计算区间的[i, j] xor 结果
        for i in range(n):
            for j in range(i, n):
                line = j - i
                param = triangle[line]
                cur = 0
                for k, x in enumerate(param):
                    if x & 1:
                        cur ^= nums[i + k]
                orv[i][j] = cur

        dp1 = [[0] * n for _ in range(n)]  # dp1[i][j] 表示在区间[i, j]上，以j为右端点的子数组xor最大值
        for j in range(n):
            dp1[j][j] = nums[j]
            for i in range(j - 1, -1, -1):
                dp1[i][j] = max(dp1[i + 1][j], orv[i][j])

        dp2 = [[0] * n for _ in range(n)]  # dp1[i][j] 表示在区间[i, j]上，所有子数组xor最大值
        for i in range(n):
            dp2[i][i] = nums[i]
            seg = orv[i][i]
            for j in range(i + 1, n):
                seg = max(seg, orv[i][j])
                dp2[i][j] = max(dp2[i][j - 1], dp1[i][j])

        ans = []
        for i, j in queries:
            ans.append(dp2[i][j])
        return ans


so = Solution()
print(so.maximumSubarrayXor(nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]))
print(so.maximumSubarrayXor(nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]))




