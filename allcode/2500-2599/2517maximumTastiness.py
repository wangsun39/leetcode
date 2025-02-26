# 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
#
# 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
#
# 返回礼盒的 最大 甜蜜度。
#
#
#
# 示例 1：
#
# 输入：price = [13,5,1,8,21,2], k = 3
# 输出：8
# 解释：选出价格分别为 [13,5,21] 的三类糖果。
# 礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
# 可以证明能够取得的最大甜蜜度就是 8 。
# 示例 2：
#
# 输入：price = [1,3,1], k = 2
# 输出：2
# 解释：选出价格分别为 [1,3] 的两类糖果。
# 礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
# 可以证明能够取得的最大甜蜜度就是 2 。
# 示例 3：
#
# 输入：price = [7,7,7,7], k = 2
# 输出：0
# 解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
#
#
# 提示：
#
# 1 <= price.length <= 105
# 1 <= price[i] <= 109
# 2 <= k <= price.length
from bisect import bisect_left
from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumTastiness1(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        def judge(val):  # 判断某个甜蜜度是否能达到
            pre = price[0]
            cnt = 0
            for i in range(1, n):
                if price[i] - pre >= val:
                    cnt += 1
                    pre = price[i]
                    if cnt >= k - 1:
                        return True
            return False

        lo, hi = 0, price[-1] - price[0]
        if judge(hi):
            return hi
        while lo < hi:   # 类型bisect_left， 找到第一个不能满足的数，它的前一个就是答案
            mid = (lo + hi) // 2
            if judge(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


    def maximumTastiness(self, price: List[int], k: int) -> int:
        # 2023/6/1  用 bisect 函数
        price.sort()
        def check(val):
            cnt = 1
            cur = price[0]
            for i, x in enumerate(price[1:], 1):
                if x - cur >= val:
                    cur = x
                    cnt += 1
                    if cnt >= k:
                        return 0  # 表示满足
            return 1  # 表示不满足
        pos = bisect_left(range(price[-1] - price[0] + 2), 1, key=lambda x: check(x))
        return pos - 1


so = Solution()
print(so.maximumTastiness(price = [1,3,1], k = 2))  # 2
print(so.maximumTastiness(price = [13,5,1,8,21,2], k = 3))  # 8
print(so.maximumTastiness(price = [144,69,103,148,184,50,129,154,2], k = 4))  # 55
print(so.maximumTastiness(price = [34,116,83,15,150,56,69,42,26], k = 6))  # 19
print(so.maximumTastiness(price = [7,7,7,7], k = 2))  # 0




