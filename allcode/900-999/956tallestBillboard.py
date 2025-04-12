# 你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。
#
# 你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。
#
# 返回 广告牌的最大可能安装高度 。如果没法安装广告牌，请返回 0 。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,6]
# 输出：6
# 解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：10
# 解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
# 示例 3：
#
# 输入：[1,2]
# 输出：0
# 解释：没法安装广告牌，所以返回 0。
#
#
# 提示：
#
# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# sum(rods[i]) <= 5000


from leetcode.allcode.competition.mypackage import *

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods) // 2
        n = len(rods)
        dp = [[-inf] * (s * 2 + 1) for _ in range(n)]  # dp[i][j] 前i项构成差值为j的正项和最大值
        dp[0][rods[0]] = rods[0]
        dp[0][-rods[0]] = 0
        for i in range(1, n):
            dp[i] = dp[i - 1][:]
            dp[i][rods[i]] = max(dp[i][rods[i]], rods[i])
            dp[i][-rods[i]] = max(dp[i][-rods[i]], 0)
            for j in range(-s, s + 1, 1):
                # 利用python的数组下标可以取负数的特性
                if -s <= j - rods[i] <= s and dp[i - 1][j - rods[i]] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - rods[i]] + rods[i])
                if -s <= j + rods[i] <= s and dp[i - 1][j + rods[i]] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + rods[i]])
        print(dp)
        return dp[-1][0] if dp[-1][0] != -inf else 0




so = Solution()
print(so.tallestBillboard([1,2,3,4,5,6]))
print(so.tallestBillboard([2,4,8,16]))
print(so.tallestBillboard([1,2]))
print(so.tallestBillboard([1,2,3,6]))

