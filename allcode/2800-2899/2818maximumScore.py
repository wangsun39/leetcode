# 给你一个长度为 n 的正整数数组 nums 和一个整数 k 。
#
# 一开始，你的分数为 1 。你可以进行以下操作至多 k 次，目标是使你的分数最大：
#
# 选择一个之前没有选过的 非空 子数组 nums[l, ..., r] 。
# 从 nums[l, ..., r] 里面选择一个 质数分数 最高的元素 x 。如果多个元素质数分数相同且最高，选择下标最小的一个。
# 将你的分数乘以 x 。
# nums[l, ..., r] 表示 nums 中起始下标为 l ，结束下标为 r 的子数组，两个端点都包含。
#
# 一个整数的 质数分数 等于 x 不同质因子的数目。比方说， 300 的质数分数为 3 ，因为 300 = 2 * 2 * 3 * 5 * 5 。
#
# 请你返回进行至多 k 次操作后，可以得到的 最大分数 。
#
# 由于答案可能很大，请你将结果对 109 + 7 取余后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [8,3,9,3,8], k = 2
# 输出：81
# 解释：进行以下操作可以得到分数 81 ：
# - 选择子数组 nums[2, ..., 2] 。nums[2] 是子数组中唯一的元素。所以我们将分数乘以 nums[2] ，分数变为 1 * 9 = 9 。
# - 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 1 ，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为 9 * 9 = 81 。
# 81 是可以得到的最高得分。
# 示例 2：
#
# 输入：nums = [19,12,14,6,10,18], k = 3
# 输出：4788
# 解释：进行以下操作可以得到分数 4788 ：
# - 选择子数组 nums[0, ..., 0] 。nums[0] 是子数组中唯一的元素。所以我们将分数乘以 nums[0] ，分数变为 1 * 19 = 19 。
# - 选择子数组 nums[5, ..., 5] 。nums[5] 是子数组中唯一的元素。所以我们将分数乘以 nums[5] ，分数变为 19 * 18 = 342 。
# - 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 2，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为  342 * 14 = 4788 。
# 4788 是可以得到的最高的分。
#
#
# 提示：
#
# 1 <= nums.length == n <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= min(n * (n + 1) / 2, 109)

from leetcode.allcode.competition.mypackage import *

def all_primes(n):
    res = [0] * n
    for i in range(2, n):
        j = 1
        if res[i]: continue
        while i * j < n:
            res[i * j] += 1
            j += 1
    return res

arr = all_primes(10 ** 5 + 1)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        nums2 = [arr[x] for x in nums]
        print(nums2)
        stack = deque()
        right = [n - i - 1 for i in range(n)]
        for i, x in enumerate(nums2):
            while stack and stack[-1][0] < x:
                v, idx = stack.pop()
                right[idx] = i - idx - 1
            stack.append([x, i])
        left = list(range(n))
        stack = deque()
        for i, x in enumerate(nums2):
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack:
                left[i] = i - stack[-1][1] - 1
            stack.append([x, i])
        print("left: ", left)
        print("right: ", right)
        ll = [[i, x] for i, x in enumerate(nums)]
        ll.sort(key=lambda x: x[1], reverse=True)
        print(ll)
        ans = 1
        for i, x in ll:
            t = (left[i] + 1) * (right[i] + 1)
            t = min(t, k)
            v = pow(x, t, MOD)
            ans *= v
            ans %= MOD
            k -= t
            if k == 0:
                break
        return ans


so = Solution()
print(so.maximumScore(nums = [19,12,14,6,10,18], k = 3))
print(so.maximumScore([3289,2832,14858,22011], 6))
print(so.maximumScore(nums = [8,3,9,3,8], k = 2))




