# 给你一个下标从 0 开始的非负整数数组 nums 和两个整数 l 和 r 。
#
# 请你返回 nums 中子多重集合的和在闭区间 [l, r] 之间的 子多重集合的数目 。
#
# 由于答案可能很大，请你将答案对 109 + 7 取余后返回。
#
# 子多重集合 指的是从数组中选出一些元素构成的 无序 集合，每个元素 x 出现的次数可以是 0, 1, ..., occ[x] 次，其中 occ[x] 是元素 x 在数组中的出现次数。
#
# 注意：
#
# 如果两个子多重集合中的元素排序后一模一样，那么它们两个是相同的 子多重集合 。
# 空 集合的和是 0 。
#
#
# 示例 1：
# 
# 输入：nums = [1,2,2,3], l = 6, r = 6
# 输出：1
# 解释：唯一和为 6 的子集合是 {1, 2, 3} 。
# 示例 2：
#
# 输入：nums = [2,1,4,2,7], l = 1, r = 5
# 输出：7
# 解释：和在闭区间 [1, 5] 之间的子多重集合为 {1} ，{2} ，{4} ，{2, 2} ，{1, 2} ，{1, 4} 和 {1, 2, 2} 。
# 示例 3：
#
# 输入：nums = [1,2,1,3,5,2], l = 3, r = 5
# 输出：9
# 解释：和在闭区间 [3, 5] 之间的子多重集合为 {3} ，{5} ，{1, 2} ，{1, 3} ，{2, 2} ，{2, 3} ，{1, 1, 2} ，{1, 1, 3} 和 {1, 2, 2} 。
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 0 <= nums[i] <= 2 * 104
# nums 的和不超过 2 * 104 。
# 0 <= l <= r <= 2 * 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubMultisets1(self, nums: List[int], l: int, r: int) -> int:
        # 性能不够 O(N^3)
        MOD = 10 ** 9 + 7
        counter = Counter(nums)
        counter = [[k, v] for k, v in counter.items()]
        n = len(counter)

        @cache
        def dfs(i, upper):
            if i == n: return 1
            ans = 0
            num, cnt = counter[i]
            for j in range(cnt + 1):
                if j * num > upper:
                    break
                ans += dfs(i + 1, upper - j * num)
                ans %= MOD
            # print(i, upper, ans)
            return ans
        v1, v2 = dfs(0, l - 1), dfs(0, r)
        return (v2 - v1 + MOD) % MOD

    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        counter = Counter(nums)
        counter = [[k, v] for k, v in counter.items()]
        n = len(counter)

        @cache
        def dfs(i, j):  # 前i个数，组成j的各种组合数
            # dp[i][j] = dp[i-1][j]+dp[i-1][j-k]+dp[i-1][j-2k]+...+dp[i-1][j-vk]
            # dp[i][j-k] =          dp[i-1][j-k]+dp[i-1][j-2k]+...+dp[i-1][j-vk]+dp[i-1][j-(v+1)k]
            if j < 0 or i < 0: return 0
            k, v = counter[i]
            if j == 0: return v + 1 if k == 0 else 1
            if k == 0: return dfs(i - 1, j)
            if i == 0: return j % k <= v
            if j < k:
                return dfs(i - 1, j) + 1
            if (v + 1) * k <= j:
                return (dfs(i, j - k) + dfs(i - 1, j) - dfs(i - 1, j - (v + 1) * k)) % MOD
            return (dfs(i, j - k) + dfs(i - 1, j)) % MOD

        return sum(dfs(n - 1, i) for i in range(l, r + 1)) % MOD


so = Solution()
print(so.countSubMultisets(nums = [1,2], l = 3, r = 3))
print(so.countSubMultisets(nums = [0,0,0,0], l = 0, r = 0))
print(so.countSubMultisets(nums = [2,1,4,2,7], l = 1, r = 5))
print(so.countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5))




