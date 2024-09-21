# 给你一个下标从 0 开始的二维整数数组 transactions，其中transactions[i] = [costi, cashbacki] 。
#
# 数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱 money ，为了完成交易 i ，money >= costi 这个条件必须为真。执行交易后，你的钱数 money 变成 money - costi + cashbacki 。
#
# 请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数 money 是多少。
#
#
#
# 示例 1：
#
# 输入：transactions = [[2,1],[5,0],[4,2]]
# 输出：10
# 解释：
# 刚开始 money = 10 ，交易可以以任意顺序进行。
# 可以证明如果 money < 10 ，那么某些交易无法进行。
# 示例 2：
#
# 输入：transactions = [[3,0],[0,3]]
# 输出：3
# 解释：
# - 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
# - 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
# 所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
#
#
# 提示：
#
# 1 <= transactions.length <= 105
# transactions[i].length == 2
# 0 <= costi, cashbacki <= 109
#
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        delta = [c - b for c, b in transactions]
        s = sum(x for x in delta if x > 0)  # 所有亏损的交易额之和
        ans = 0
        n = len(transactions)
        for i in range(n):
            c, b = transactions[i]
            if c - b > 0:
                ans = max(ans, s - (c - b) + c)
            else:
                ans = max(ans, s + c)
        return ans


    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 2024/9/21 贪心，先处理亏的交易，再处理赢的交易
        # 亏的交易按卖出价从小到大排序，赢的交易按买入从大到小排序
        t1, t2 = [], []
        for x, y in transactions:
            if x < y:
                t2.append([x, y])
            else:
                t1.append([x, y])
        t1.sort(key=lambda x: x[1])
        t2.sort(reverse=True)
        cur = 0
        ans = 0
        for x, y in t1:
            if cur < x:
                ans += (x - cur)
                cur = y
        if t2 and cur < t2[0][0]:
            ans += t2[0][0] - cur
        return ans

so = Solution()
print(so.minimumMoney(transactions = [[2,1],[5,0],[4,2]]))
print(so.minimumMoney(transactions = [[3,0],[0,3]]))




