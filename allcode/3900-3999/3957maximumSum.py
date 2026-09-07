# 给你一个长度为 n 的整数数组 nums，以及三个整数 m、l 和 r。
#
# 每个被选择的 子数组 的长度都在 [l, r] 范围内（包含两端）。
# 所有被选择 子数组 的总和 最大 。
# 返回你能够取得的 最大 总和。
#
# 子数组 是数组中一个连续的 非空 元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [4,1,-5,2], m = 2, l = 1, r = 3
#
# 输出： 7
#
# 解释：
#
# 一种最优策略是：
#
# 选择子数组 [4, 1]，其和为 4 + 1 = 5；再选择子数组 [2]，其和为 2。两个子数组的长度都在 [l, r] 范围内。
# 这些子数组的总和为 5 + 2 = 7，这是在至多 m = 2 个子数组下能够取得的最大总和。
# 示例 2：
#
# 输入： nums = [1,0,3,4], m = 2, l = 1, r = 2
#
# 输出： 8
#
# 解释：
#
# 一种最优策略是：
#
# 选择子数组 [1]，其和为 1；再选择子数组 [3, 4]，其和为 3 + 4 = 7。两个子数组的长度都在 [l, r] 范围内。
# 这些子数组的总和为 1 + 7 = 8，这是在至多 m = 2 个子数组下能够取得的最大总和。
# 示例 3：
#
# 输入： nums = [-1,7,-4], m = 1, l = 2, r = 3
#
# 输出： 6
#
# 解释：
#
# 选择 nums 中的子数组 [-1, 7]，其长度在 [l, r] 范围内。
# 该子数组的总和为 -1 + 7 = 6，这是在至多 m = 1 个子数组下能够取得的最大总和。
# 示例 4：
#
# 输入： nums = [-3,-4,-1], m = 2, l = 1, r = 2
#
# 输出： -1
#
# 解释：
#
# nums 的所有子数组和均为负数。最优策略是选择子数组 [-1]，它的长度在 [l, r] 范围内。
# 该子数组的总和为 -1，这是在至多 m = 2 个子数组下能够取得的最大总和。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= m <= n
# 1 <= l <= r <= n

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        def calc(val):
            #nums中选取任意多个子数组， 目标 f = 子数组总和-val*子数组个数，求f的最大值
            # val 就是一个惩罚因子
            dp = [0] * n   # 前n个数的f值
            dp2 = [0] * n  # 达到f]i]对应的最少分组个数
            # 1. dp[i] = dp[i-1]
            # 2. dp[i] = max(dp[j] + s[i + 1] - s[j + 1] - val)  其中 l <= i - j <= r
            dq = deque()  # 单调减的队列 存放 [dp[i]-s[i+1], i]
            res = [-inf, 0]
            for i in range(l - 1, n):
                # 处理第i项时，i为当前段的右端点，那么左端点的前一个位置位于 [i - r, i - l] 区间内，不在这个区间的要popleft，i - l 进入这个区间的要 append
                if dq and dq[0][1] < i - r:
                    dq.popleft()
                while dq and dq[-1][0] < dp[i - l] - s[i + 1 - l]:
                    dq.pop()
                if i == l - 1:
                    dq.append([0, -1])  # 这是第一个区间
                else:
                    dq.append([dp[i - l] - s[i + 1 - l], i - l])

                head = dq[0]
                if head[1] != -1:
                    resi = [head[0] + s[i + 1] - val, dp2[head[1]] + 1]
                else:
                    resi = [head[0] + s[i + 1] - val, 1]   # 从 nums[0] 到 nums[i]的完整子数组

                # 这里的 resi 一定是选取了一些元素产生的最小子数组和，不会是选到一个空数组，因此可以用这个更新返回值
                if res[0] < resi[0]:
                    res = resi[:]
                elif res[1] > resi[1]:   # 子数组和相同时，选使用子数组个数少的那个
                    res = resi[:]

                # 用resi 更新dp/dp2
                if i > 0:
                    if resi[0] < dp[i - 1]:
                        dp[i] = dp[i - 1]
                        dp2[i] = dp2[i - 1]
                    elif resi[0] > dp[i - 1]:
                        dp[i] = resi[0]
                        dp2[i] = resi[1]
                    else:
                        # dp[i - 1] 和 resi 产生的最大值相同时，子数组个数选它们之中小的
                        dp[i] = dp[i - 1]
                        dp2[i] = MIN(dp2[i - 1], resi[1])
                else:
                    if res[0] > 0:
                        dp[i] = res[0]
                        dp2[i] = 1

            # 返回值要用res，而不能用dp，因为dp中的数值初始化为0，不能保证一定能取到一组有效子数组
            return res

        v, cnt = calc(0)
        if cnt <= m:
            return v

        lo, hi = 0, sum(x for x in nums if x > 0) + 1
        # 初始的上界是所有正数之和，此时只要选择一个子数组，则f的值都是负数，选的越多负值越多，因此这个惩罚因子已经足够大
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            v, cnt = calc(mid)
            if cnt > m:
                # 子数组数量多，就加大惩罚
                lo = mid
            elif cnt < m:
                hi = mid
                ans = v + mid * m
            else:
                return v + mid * m

        # 如果二分结束还没返回，取最接近的
        return ans




so = Solution()
print(so.maximumSum(nums = [-39,30,-67,21,-22,42,30,-66], m = 2, l = 1, r = 1))  # 26
print(so.maximumSum(nums = [8,11,15], m = 2, l = 1, r = 1))  # 26
print(so.maximumSum(nums = [14,5], m = 1, l = 1, r = 1))  # -1
print(so.maximumSum(nums = [-3,-4,-1], m = 2, l = 1, r = 2))  # -1
print(so.maximumSum(nums = [4,1,-5,2], m = 2, l = 1, r = 3))  # 7
print(so.maximumSum(nums = [43,28,42,9,-36,-12], m = 3, l = 1, r = 1))  # 113
print(so.maximumSum(nums = [1,0,3,4], m = 2, l = 1, r = 2))  # 8
print(so.maximumSum(nums = [14,5], m = 1, l = 1, r = 1))  # 14
print(so.maximumSum(nums = [-1,7,-4], m = 1, l = 2, r = 3))  # 6




