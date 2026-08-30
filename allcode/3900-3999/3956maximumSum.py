# 给你一个长度为 n 的整数数组 nums，以及三个整数 m、l 和 r。
#
# 你的任务是从 nums 中选择 至少 一个且 至多 m 个 互不重叠的子数组，并满足：
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
# 1 <= n == nums.length <= 1000
# -109 <= nums[i] <= 109
# 1 <= m <= n
# 1 <= l <= r <= n

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        dp = [[-inf] * n for _ in range(m + 1)]  # 前j个数组成i个子数组的最大和
        for i in range(n):
            dp[0][i] = 0

        # dp[i][j] = max(dp[i - 1][k] + s[j + 1] - s[k + 1])    (l<=j-k<=r 即 j-r<=k<=j-l)
        # dp[i][j] = max(dp[i - 1][k] - s[k + 1]) + s[j + 1]    (j-r<=k<=j-l)
        # 需要将这个范围内的  dp[i - 1][k] - s[k + 1]  放入堆中

        ans = -inf
        for i in range(1, m + 1):
            deleted = Counter()  # 堆中已删除计数
            hp = []

            for j in range(i * l - 1, n):
                # k 的窗口滑到 [j-r, j-l] 区间
                if j - r - 1 >= 0:
                    L = dp[i - 1][j - r - 1] - s[j - r - 1 + 1]
                    deleted[-L] += 1
                if j - l >= 0:
                    R = dp[i - 1][j - l] - s[j - l + 1]
                    heappush(hp, -R)
                while hp:
                    top = hp[0]
                    if deleted[top] > 0:
                        heappop(hp)
                        deleted[top] -= 1
                    else:
                        break
                if hp:
                    dp[i][j] = -hp[0] + s[j + 1]
                    if i == 1 and l <= j + 1 <= r:
                        dp[i][j] = MAX(dp[i][j], s[j + 1])  # 前缀是一个子数组的情况
                else:
                    dp[i][j] = 0 + s[j + 1]
                if j > 0:
                    dp[i][j] = MAX(dp[i][j], dp[i][j - 1])


        # print(dp)
        for i in range(1, m + 1):
            ans = MAX(ans, dp[i][-1])
        return ans


so = Solution()
print(so.maximumSum(nums = [4,1,-5,2], m = 2, l = 1, r = 3))  # 7
print(so.maximumSum(nums = [43,28,42,9,-36,-12], m = 3, l = 1, r = 1))  # 113
print(so.maximumSum(nums = [1,0,3,4], m = 2, l = 1, r = 2))  # 8
print(so.maximumSum(nums = [14,5], m = 1, l = 1, r = 1))  # 14
print(so.maximumSum(nums = [-1,7,-4], m = 1, l = 2, r = 3))  # 6




