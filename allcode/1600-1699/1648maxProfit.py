# 你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。
#
# 这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。比方说还剩下 6 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5 （也就是球的价值随着顾客购买同色球是递减的）
#
# 给你整数数组 inventory ，其中 inventory[i] 表示第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。你可以按照 任意顺序 卖球。
#
# 请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 109 + 7 取余数 的结果。
#
#
#
# 示例 1：
#
#
# 输入：inventory = [2,5], orders = 4
# 输出：14
# 解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
# 最大总和为 2 + 5 + 4 + 3 = 14 。
# 示例 2：
#
# 输入：inventory = [3,5], orders = 6
# 输出：19
# 解释：卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。
# 最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。
# 示例 3：
#
# 输入：inventory = [2,8,4,10,6], orders = 20
# 输出：110
# 示例 4：
#
# 输入：inventory = [1000000000], orders = 1000000000
# 输出：21
# 解释：卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 109 + 7 取余为 21 。
#
#
# 提示：
#
# 1 <= inventory.length <= 105
# 1 <= inventory[i] <= 109
# 1 <= orders <= min(sum(inventory[i]), 109)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7
        counter = Counter(inventory)
        counter = [[x, num] for x, num in counter.items()]
        counter.append([0, 0]) # 增加一个哨兵
        counter.sort()
        n = len(counter)
        ans = 0
        s = 0
        for i in range(n - 1, 0, -1):
            x, num = counter[i]
            y, _ = counter[i - 1]
            s += num
            ss = (x + y + 1) * (x - y) // 2 * s # 从 y + 1 累加到 x，本轮总订单价值
            ss_num = (x - y) * s  # 本轮总订单数
            if ss_num < orders:
                ans += ss
                ans %= MOD
                orders -= ss_num
            else:
                q, r = divmod(orders, s)
                ans += ((x + x - q + 1) * q // 2 * s)
                ans += r * (x - q)
                ans %= MOD
                return ans



so = Solution()
print(so.maxProfit(inventory = [497978859,167261111,483575207,591815159], orders = 836556809))
print(so.maxProfit(inventory = [2,5], orders = 4))
print(so.maxProfit(inventory = [3,5], orders = 6))
print(so.maxProfit(inventory = [2,8,4,10,6], orders = 20))
print(so.maxProfit(inventory = [1000000000], orders = 1000000000))




