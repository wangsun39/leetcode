# 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：
#
# 如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
# 如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
# 如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：
#
# 在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
# 在关门期间，如果某一个小时有顾客到达，代价增加 1 。
# 请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
#
# 注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。
#
#
#
# 示例 1：
#
# 输入：customers = "YYNY"
# 输出：2
# 解释：
# - 第 0 小时关门，总共 1+1+0+1 = 3 代价。
# - 第 1 小时关门，总共 0+1+0+1 = 2 代价。
# - 第 2 小时关门，总共 0+0+0+1 = 1 代价。
# - 第 3 小时关门，总共 0+0+1+1 = 2 代价。
# - 第 4 小时关门，总共 0+0+1+0 = 1 代价。
# 在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
# 示例 2：
#
# 输入：customers = "NNNNN"
# 输出：0
# 解释：最优关门时间是 0 ，因为自始至终没有顾客到达。
# 示例 3：
#
# 输入：customers = "YYYY"
# 输出：4
# 解释：最优关门时间是 4 ，因为每一小时均有顾客到达。
#
#
# 提示：
#
# 1 <= customers.length <= 105
# customers 只包含字符 'Y' 和 'N' 。
from leetcode.allcode.competition.mypackage import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers += 'N'
        n = len(customers)
        # s1, s2 = [0 if customers[0] == 'Y' else 1], [1 if customers[-1] == 'Y' else 0]
        s1, s2 = [0] * n, [0] * n
        if customers[0] == 'N':
            s1[0] = 1
        if customers[-1] == 'Y':
            s2[n - 1] = 1
        for i in range(1, n):
            s1[i] = s1[i - 1]
            if customers[i] == 'N':
                s1[i] += 1
        # for c in customers[n - 2::-1]:
        for i in range(n - 2, -1, -1):
            s2[i] = s2[i + 1]
            if customers[i] == 'Y':
                s2[i] += 1
        # print(s1, s2)
        cost = s2[0]
        ans = 0
        for i in range(1, n):
            if s1[i - 1] + s2[i] < cost:
                cost = s1[i - 1] + s2[i]
                ans = i
        # if cost > s1[-1]:
        #     return n
        return ans


so = Solution()
print(so.bestClosingTime("YNYY"))
print(so.bestClosingTime("YYNY"))
print(so.bestClosingTime("NNNNN"))
print(so.bestClosingTime("YYYY"))




