# 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
#
# 请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,0,1,0,1], k = 2
# 输出：1
# 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。
# 示例 2：
#
# 输入：nums = [1,0,0,0,0,0,1,1], k = 3
# 输出：5
# 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。
# 示例 3：
#
# 输入：nums = [1,1,0,1], k = 2
# 输出：0
# 解释：nums 已经有连续 2 个 1 了。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 要么是 0 ，要么是 1 。
# 1 <= k <= sum(nums)



# Definition for a binary tree node.
from typing import List
class Solution:
    def minMoves1(self, nums: List[int], k: int) -> int:
        idx = [i for i, e in enumerate(nums) if e == 1]
        l_idx = len(idx)
        # idx 数组进行长度为k的滑动窗口
        # l = r = 0
        if k & 1:
            mid = k // 2  # 中位数的下标
            l = sum(idx[i] for i in range(mid))
            r = sum(idx[i] for i in range(mid + 1, k))
            ans = r - l
            for i in range(1, l_idx - k + 1):
                mid += 1
                l -= idx[i - 1]
                l += idx[mid - 1]
                r += idx[i + k - 1]
                r -= idx[mid]
                ans = min(ans, r - l)
            return ans - (k * k - 1) // 4
        else:
            mid = k // 2  # 中位数的下标
            l = sum(idx[i] for i in range(mid))
            r = sum(idx[i] for i in range(mid, k))
            ans = r - l
            for i in range(1, l_idx - k + 1):
                mid += 1
                l -= idx[i - 1]
                l += idx[mid - 1]
                r += idx[i + k - 1]
                r -= idx[mid - 1]
                ans = min(ans, r - l)
            return ans - k * k // 4

    def minMoves(self, nums: List[int], k: int) -> int:
        # 2023/2/8
        # 用灵神的解法 https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solution/tu-jie-zhuan-huan-cheng-zhong-wei-shu-ta-iz4v/
        pi = []  # pi 记录所有1下标的前j
        j = 0
        for i, x in enumerate(nums):
            if x == 1:
                pi.append(i - j)
                j += 1
        n = len(pi)
        if k & 1:
            mid = (k - 1) // 2
            l = sum(pi[mid] - x for x in pi[:mid])
            r = sum(x - pi[mid] for x in pi[mid + 1: k])
            ans = cur = l + r
            begin, end = 0, k - 1
            for _ in range(n - k):
                cur += (-(pi[mid] - pi[begin]) + (pi[end + 1] - pi[mid + 1]))
                ans = min(ans, cur)
                begin += 1
                end += 1
                mid += 1
        else:
            mid = (k - 1) // 2
            l = sum(pi[mid] - x for x in pi[:mid])
            r = sum(x - pi[mid] for x in pi[mid + 1: k])
            ans = cur = l + r
            begin, end = 0, k - 1
            for _ in range(n - k):
                cur += (-(pi[mid] - pi[begin]) + (pi[end + 1] - pi[mid + 1]) - (pi[mid + 1] -pi[mid]))
                ans = min(ans, cur)
                begin += 1
                end += 1
                mid += 1
        return ans

so = Solution()

print(so.minMoves(nums = [1,0,0,1,0,1], k = 2))  # 1
print(so.minMoves(nums = [1,1,0,1], k = 2))  # 0
print(so.minMoves(nums = [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 14))  # 1
print(so.minMoves(nums = [1,0,0,1,0,1,1,1,0,1,1], k = 7))  # 6
print(so.minMoves(nums = [1,0,0,0,0,0,1,1], k = 3))  # 5


