# 给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。
#
# 你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。
#
# 返回使用这些硬币能制造的 第 kth 小 金额。
#
#
#
# 示例 1：
#
# 输入： coins = [3,6,9], k = 3
#
# 输出： 9
#
# 解释：给定的硬币可以制造以下金额：
# 3元硬币产生3的倍数：3, 6, 9, 12, 15等。
# 6元硬币产生6的倍数：6, 12, 18, 24等。
# 9元硬币产生9的倍数：9, 18, 27, 36等。
# 所有硬币合起来可以产生：3, 6, 9, 12, 15等。
#
# 示例 2：
#
# 输入：coins = [5,2], k = 7
#
# 输出：12
#
# 解释：给定的硬币可以制造以下金额：
# 5元硬币产生5的倍数：5, 10, 15, 20等。
# 2元硬币产生2的倍数：2, 4, 6, 8, 10, 12等。
# 所有硬币合起来可以产生：2, 4, 5, 6, 8, 10, 12, 14, 15等。
#
#
#
# 提示：
#
# 1 <= coins.length <= 15
# 1 <= coins[i] <= 25
# 1 <= k <= 2 * 109
# coins 包含两两不同的整数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        m = 1 << n
        lcm_ = [0] * m
        for i in range(n):
            lcm_[1 << i] = coins[i]
        for i in range(1, m):
            if i.bit_count() == 1: continue
            j = i & (i - 1)  # 将i最右边的1置为0(去掉最右边的1)
            t = (i & (-i)).bit_length() - 1  # i最右的1对应的下标
            lcm_[i] = lcm(lcm_[j], coins[t])

        def check(val):
            cnt = 0
            for i in range(1, m):
                v = i.bit_count()
                if v & 1:  # 1的个数是奇数为+，否则为-
                    cnt += val // lcm_[i]
                else:
                    cnt -= val // lcm_[i]
            return cnt >= k

        lo, hi = k - 1, min(coins) * k
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.findKthSmallest(coins = [5,2], k = 7))
print(so.findKthSmallest(coins = [3,6,9], k = 3))




