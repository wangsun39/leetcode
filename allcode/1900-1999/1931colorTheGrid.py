# 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
#
# 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
#
# 输入：m = 1, n = 1
# 输出：3
# 解释：如上图所示，存在三种可能的涂色方案。
# 示例 2：
#
#
# 输入：m = 1, n = 2
# 输出：6
# 解释：如上图所示，存在六种可能的涂色方案。
# 示例 3：
#
# 输入：m = 5, n = 5
# 输出：580986
#
#
# 提示：
#
# 1 <= m <= 5
# 1 <= n <= 1000

from leetcode.allcode.competition.mypackage import *


def dfs(i, j, mx):
    res = []
    if i == mx:
        for k in range(3):
            if k != j:
                res.append([k])
    else:
        for k in range(3):
            if k != j:
                l = dfs(i + 1, k, mx)
                for t in range(len(l)):
                    l[t] = [k] + l[t]
                res += l
    return res


l = []
ld = []
for i in range(5):
    l.append(dfs(0, -1, i))
    adj = defaultdict(list)
    for l1 in l[-1]:
        for l2 in l[-1]:
            if all(l1[j] != l2[j] for j in range(i + 1)):
                adj[tuple(l1)].append(tuple(l2))
    ld.append(adj)
# print(ld[1])


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp1 = {tu: 1 for tu in ld[m - 1].keys()}
        for _ in range(n - 1):
            dp2 = defaultdict(int)
            for tu1 in dp1.keys():
                for tu2 in ld[m - 1][tu1]:
                    dp2[tu2] += dp1[tu1]
                    dp2[tu2] %= MOD
            dp1 = dp2
        return sum(dp1.values()) % MOD



so = Solution()
print(so.colorTheGrid(m = 1, n = 1))
print(so.colorTheGrid(m = 1, n = 2))
print(so.colorTheGrid(m = 5, n = 5))
print(so.colorTheGrid(m = 5, n = 100))




