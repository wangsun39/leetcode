# 给你一个正整数数组 nums 和一个整数 k 。
#
# 分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。
#
# 返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。
#
# 如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4], k = 4
# 输出：6
# 解释：好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) 和 ([4], [1,2,3]) 。
# 示例 2：
#
# 输入：nums = [3,3,3], k = 4
# 输出：0
# 解释：数组中不存在好分区。
# 示例 3：
#
# 输入：nums = [6,6], k = 2
# 输出：2
# 解释：可以将 nums[0] 放入第一个分区或第二个分区中。
# 好分区的情况是 ([6], [6]) 和 ([6], [6]) 。
#
#
# 提示：
#
# 1 <= nums.length, k <= 1000
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPartitions1(self, nums: List[int], k: int) -> int:
        if sum(nums) < k * 2: return 0
        MOD = 10 ** 9 + 7
        n = len(nums)
        pre = [1 if i + 1 <= nums[0] else 2 for i in range(k)]  # 1 表示空集，2表示空集 + {nums[0]}
        # print(pre)
        dp = [0] * k  # dp[j] 子集的和小于 j+1 的子集个数
        for i in range(1, n):
            for j in range(k):
                if j >= nums[i]:
                    dp[j] = pre[j - nums[i]] + pre[j]
                    dp[j] %= MOD
                else:
                    dp[j] = pre[j]
            pre, dp = dp, [0] * k
            # print(pre)
        return ((pow(2, n, MOD) + MOD) - pre[-1] * 2) % MOD

    def countPartitions(self, nums: List[int], k: int) -> int:
        # 2023/1/30 重新写了一遍
        MOD = 10 ** 9 + 7
        s = sum(nums)
        if s < 2 * k: return 0
        n = len(nums)
        dp = [[0] * (1000) for _ in range(n)]  # dp[i][j]  前 i + 1 个数中和 == j 的子集个数
        dp[0][0] = 1   # 空集
        if nums[0] < 1000: dp[0][nums[0]] = 1
        for i in range(1, n):
            for j in range(1000):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i]]
        total = pow(2, n, MOD) + MOD
        return (total - sum(dp[-1][:k]) * 2) % MOD


so = Solution()
print(so.countPartitions(nums = [6,6], k = 2))  # 2
print(so.countPartitions(nums = [3,3,3], k = 4))  # 0
print(so.countPartitions(nums = [1,2,3,4], k = 4))  # 6




