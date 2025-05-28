# 给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：
#
# 第 i 位顾客 恰好 有 quantity[i] 个整数。
# 第 i 位顾客拿到的整数都是 相同的 。
# 每位顾客都满足上述两个要求。
# 如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4], quantity = [2]
# 输出：false
# 解释：第 0 位顾客没办法得到两个相同的整数。
# 示例 2：
#
# 输入：nums = [1,2,3,3], quantity = [2]
# 输出：true
# 解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
# 示例 3：
#
# 输入：nums = [1,1,2,2], quantity = [2,2]
# 输出：true
# 解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= 1000
# m == quantity.length
# 1 <= m <= 10
# 1 <= quantity[i] <= 105
# nums 中至多有 50 个不同的数字。

from leetcode.allcode.competition.mypackage import *


# Definition for a binary tree node.
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = Counter(nums)
        counter = list(counter.values())
        n, m = len(counter), len(quantity)

        s = [0] * (1 << m)  # 预处理所有bits对应的quantity之和
        for i in range(1 << m):
            for j in range(m):
                if i & (1 << j):
                    s[i] += quantity[j]

        @cache
        def dfs(idx, bits):  # 用bits描述对 quantity 覆盖情况
            # 返回前idx个counter，是否能覆盖bits对应的 quantity
            if bits == 0:
                return True
            if idx == 0:
                return counter[idx] >= s[bits]

            # 遍历bits的所有子集
            sub = bits
            while True:
                # 处理 sub 的逻辑
                c = bits - sub  # bits中除了 sub的子集
                if counter[idx] >= s[c] and dfs(idx - 1, sub):
                    return True
                sub = (sub - 1) & bits
                if sub == bits:
                    break

            return False

        return dfs(n - 1, (1 << m) - 1)




so = Solution()
print(so.canDistribute(nums = [1,2,3,3], quantity = [2]))   # True
print(so.canDistribute(nums = [1,2,3,4], quantity = [2]))   # False






