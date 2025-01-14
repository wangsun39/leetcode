# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列
# 。
#
#
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
#
# 进阶：
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?

import bisect
import math
from typing import List
class Solution1:
    def lengthOfLIS1(self, nums):
        number = len(nums)
        if number == 0:
            return 0
        A = [0] * number
        A[0] = 1
        # A[i] 表示以nums[i]结尾的最大字序长度
        for i in range(1, number):
            if nums[i] == nums[i-1]:
                A[i] = A[i-1]
            else:
                max_v = 1
                for j in range(i):
                    #print(max_v, i, j)
                    if nums[i] > nums[j]:
                        max_v = max(max_v, A[j]+1)
                A[i] = max_v
        print(A)
        return max(A)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 2023/1/20  一维DP  O(n^2)
        n = len(nums)
        dp = [1] * n  # dp[i] 表示以 nums[:i+1] 中的最长递增子序列长度
        for i, x in enumerate(nums):
            cur_mx = 1
            for j in range(i):
                if x > nums[j]:
                    cur_mx = max(cur_mx, dp[j] + 1)
            dp[i] = cur_mx
        return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 2023/1/20  单调栈 + 二分  O(nlogn)
        stack = [nums[0]]  # 单调栈
        for i, x in enumerate(nums):
            if len(stack) == 0 or x > stack[-1]:
                stack.append(x)
                continue
            pos = bisect.bisect_left(stack, x)
            stack[pos] = x
        return len(stack)


class Fenwick2:
    # 求前缀最大值
    # 所有函数参数下标从1开始
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        self.f = [0] * (n + 1)   # 关键区间最大值

    def update(self, i: int, val: int) -> None:  # nums[i] = val
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def query(self, i: int) -> int:  # 下标<=i的最大值
        mx = 0
        while i > 0:
            mx = max(mx, self.f[i])
            i &= i - 1
        return mx

class Solution:
    # 2025/1/13 树状数组解法
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [x + 10000 for x in nums]
        mx = max(nums)
        fw = Fenwick2(mx + 1)
        for x in nums:
            val = fw.query(x)  # 查询树状数组中保存的 < x 的最大值
            fw.update(x + 1, val + 1)
        return fw.query(mx + 1)

so = Solution()
print(so.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(so.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

