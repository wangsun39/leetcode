# 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。
#
# 请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。
#
# 答案保证在 32 位有符号整数范围以内。
#
#
#
# 示例 1：
#
#
#
# 输入：houses = [1,4,8,10,20], k = 3
# 输出：5
# 解释：将邮筒分别安放在位置 3， 9 和 20 处。
# 每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
# 示例 2：
#
#
#
# 输入：houses = [2,3,5,12,18], k = 2
# 输出：9
# 解释：将邮筒分别安放在位置 3 和 14 处。
# 每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
# 示例 3：
#
# 输入：houses = [7,4,6,1], k = 1
# 输出：8
# 示例 4：
#
# 输入：houses = [3,6,14,10], k = 4
# 输出：0
#
#
# 提示：
#
# n == houses.length
# 1 <= n <= 100
# 1 <= houses[i] <= 10^4
# 1 <= k <= n
# 数组 houses 中的整数互不相同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        def f(i, j):  # 计算从houses[i, j]范围内放置一个邮筒的最小总距离
            # 取中位数，而不是平均数
            mid = (i + j) // 2
            return sum(abs(houses[i] - houses[mid]) for i in range(i, j + 1))

        dp = [[inf] * k for _ in range(n)]  # dp[i][j] 表示 前i个房子，放置j的邮筒的最小距离
        for i in range(k): dp[i][i] = 0
        for i in range(n):
            for j in range(min(i, k)):
                if j == 0:
                    dp[i][j] = f(0, i)
                    continue
                for t in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[t][j - 1] + f(t + 1, i))
        return dp[-1][-1]


so = Solution()
print(so.minDistance([1,3,13,7,6], 2))
print(so.minDistance(houses = [1,4,8,10], k = 2))
print(so.minDistance(houses = [1,4,8,10,20], k = 3))
print(so.minDistance(houses = [2,3,5,12,18], k = 2))
print(so.minDistance(houses = [7,4,6,1], k = 1))
print(so.minDistance(houses = [3,6,14,10], k = 4))




