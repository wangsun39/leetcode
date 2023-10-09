# 给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
#
# 一个子集的 不兼容性 是该子集里面最大值和最小值的差。
#
# 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
#
# 子集的定义是数组中一些数字的集合，对数字顺序没有要求。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,4], k = 2
# 输出：4
# 解释：最优的分配是 [1,2] 和 [1,4] 。
# 不兼容性和为 (2-1) + (4-1) = 4 。
# 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
# 示例 2：
#
# 输入：nums = [6,3,8,1,3,1,2,2], k = 4
# 输出：6
# 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
# 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
# 示例 3：
#
# 输入：nums = [5,3,3,6,3,3], k = 3
# 输出：-1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
#
#
# 提示：
#
# 1 <= k <= nums.length <= 16
# nums.length 能被 k 整除。
# 1 <= nums[i] <= nums.length
from functools import cache
from math import inf
from typing import Optional, List
from collections import defaultdict, Counter


# Definition for a binary tree node.
class Solution:
    def minimumIncompatibility1(self, nums: List[int], k: int) -> int:
        # 在处理掉一些特殊用例的情况下，这个记忆化搜索算法勉强通过
        n = len(nums)
        ct = Counter(nums)
        if max(ct.values()) > k: return -1
        if k == n: return 0
        g = [-1] * (2 ** n)  # 预处理计算每个状态的不兼容性
        for i in range(2 ** n):
            if i.bit_count() != n // k: continue
            s = set()
            skip = False
            for j in range(n):
                if i & (1 << j) == 0: continue
                if nums[j] in s:
                    skip = True
                    break
                s.add(nums[j])
            if skip: continue
            g[i] = max(s) - min(s)

        @cache
        def dfs(mask):
            if mask == 0: return 0
            sub = mask
            res = inf
            while sub:
                if g[sub] != -1:
                    res = min(res, dfs(mask & ~sub) + g[sub])
                sub = (sub - 1) & mask
            return res
        return dfs(2 ** n - 1)

    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # 改为DP版本
        n = len(nums)
        ct = Counter(nums)
        if max(ct.values()) > k: return -1
        if k == n: return 0
        g = [-1] * (2 ** n)  # 预处理计算每个状态的不兼容性
        for i in range(2 ** n):
            if i.bit_count() != n // k: continue
            s = set()
            skip = False
            for j in range(n):
                if i & (1 << j) == 0: continue
                if nums[j] in s:
                    skip = True
                    break
                s.add(nums[j])
            if skip: continue
            g[i] = max(s) - min(s)

        dp = [inf] * (2 ** n)
        dp[0] = 0
        for i in range(2 ** n):
            if dp[i] == inf: continue  # 这个continue 可以决定是不是能通过
            mask = ((2 ** n - 1) ^ i) & (2 ** n - 1)
            s = set()
            for j in range(mask.bit_length()):
                if mask & (1 << j):
                    if nums[j] not in s:
                        s.add(nums[j])
                    else:
                        mask &= ~(1 << j)
            sub = mask
            while sub:
                if sub.bit_count() == n // k:
                    dp[i | sub] = min(dp[i | sub], dp[i] + g[sub])
                sub = (sub - 1) & mask

        return dp[-1]


so = Solution()

print(so.minimumIncompatibility(nums = [1,2,1,4], k = 2))   # 4
print(so.minimumIncompatibility(nums = [6,3,8,1,3,1,2,2], k = 4))
print(so.minimumIncompatibility(nums = [1, 1], k = 1))
print(so.minimumIncompatibility(nums = [1], k = 1))
print(so.minimumIncompatibility(nums = [5,3,3,6,3,3], k = 3))




