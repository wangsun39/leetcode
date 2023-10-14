# 给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：
#
# 对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
# 请你返回特别排列的总数目，由于答案可能很大，请将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,6]
# 输出：2
# 解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。
# 示例 2：
#
# 输入：nums = [1,4,3]
# 输出：2
# 解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
#
#
# 提示：
#
# 2 <= nums.length <= 14
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        pair = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    pair[i].append(j)
                    pair[j].append(i)
        ans = 0
        MOD = 10 ** 9 + 7

        @cache
        def dfs(idx, mask): # 以 idx 开头的不同总数
            if mask == 0: return 1
            res = 0
            for idy in pair[idx]:
                if mask & (1 << idy) == 0: continue
                res += dfs(idy, mask & (~(1 << idy)))
                res %= MOD
            return res

        for i in range(n):
            ans += dfs(i, (2 ** n - 1) & (~(1 << i)))
            ans %= MOD

        return ans


so = Solution()
print(so.specialPerm([2,3,6]))
print(so.specialPerm([1,4,3]))




