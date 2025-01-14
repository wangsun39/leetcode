# 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
#
# 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
#
# 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。
#
#
#
# 示例 1：
#
# 输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# 输出：34
# 解释：你可以选中所有球员。
# 示例 2：
#
# 输入：scores = [4,5,6,5], ages = [2,1,2,1]
# 输出：16
# 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
# 示例 3：
#
# 输入：scores = [1,2,3,5], ages = [8,9,10,1]
# 输出：6
# 解释：最佳的选择是前 3 名球员。
#
#
# 提示：
#
# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 106
# 1 <= ages[i] <= 1000





from leetcode.allcode.competition.mypackage import *

class Fenwick2:
    # 求前缀最大值
    # 所有函数参数下标从1开始
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        self.f = [0] * (n + 1)   # 关键区间最大值

    def update(self, i: int, val: int) -> None:  # nums[i] = val
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def query(self, i: int) -> int:  # 下标<=i的最大值
        mx = 0
        while i > 0:
            mx = max(mx, self.f[i])
            i &= i - 1
        return mx

# Definition for a binary tree node.
class Solution:
    def bestTeamScore1(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pair = [[ages[i], scores[i]] for i in range(n)]
        pair.sort()
        dp = [pair[i][1] for i in range(n)]  # 以 i 结尾的最大总得分
        dp[0] = pair[0][1]
        ans = dp[0]
        for i in range(1, n):
            for j in range(i):
                if pair[j][1] <= pair[i][1]:
                    if dp[i] < pair[i][1] + dp[j]:
                        dp[i] = pair[i][1] + dp[j]
                        ans = max(ans, dp[i])
        print(dp)
        return ans

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # n = len(scores)
        fw = Fenwick2(max(ages) + 1)
        ans = 0
        for score, age in sorted(zip(scores, ages)):
            pre_score = fw.query(age)
            ans = max(ans, pre_score + score)
            fw.update(age, pre_score + score)
        return ans

so = Solution()
print(so.bestTeamScore(scores = [1], ages = [4]))
print(so.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))
print(so.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(so.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))





