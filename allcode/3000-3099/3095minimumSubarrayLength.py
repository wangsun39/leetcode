# 给你一个 非负 整数数组 nums 和一个整数 k 。
#
# 如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。
#
# 请你返回 nums 中 最短特别非空
# 子数组
# 的长度，如果特别子数组不存在，那么返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3], k = 2
#
# 输出：1
#
# 解释：
#
# 子数组 [3] 的按位 OR 值为 3 ，所以我们返回 1 。
#
# 示例 2：
#
# 输入：nums = [2,1,8], k = 10
#
# 输出：3
#
# 解释：
#
# 子数组 [2,1,8] 的按位 OR 值为 11 ，所以我们返回 3 。
#
# 示例 3：
#
# 输入：nums = [1,2], k = 0
#
# 输出：1
#
# 解释：
#
# 子数组 [1] 的按位 OR 值为 1 ，所以我们返回 1 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = [0] * 32  # counter[i][j]  表示前i个树中第j列累计有多少个1
        right = 1
        def trans():  # 把counter转换成对应的数字
            v = 0
            for i in range(32):
                if counter[i]:
                    v += (1 << i)
            return v
        def add(v):  # 把v加到counter中
            for i in range(32):
                if v & (1 << i):
                    counter[i] += 1
        def sub(v):  # 把v减到counter中
            for i in range(32):
                if v & (1 << i):
                    counter[i] -= 1
        if k == 0:
            return 1
        ans = inf
        add(nums[0])
        for i, x in enumerate(nums):
            if i > 0:
                sub(nums[i - 1])
            while right < n:
                if trans() < k:
                    add(nums[right])
                    right += 1
                else:
                    break
            if trans() < k:
                break
            ans = min(ans, right - i)
        if ans < inf:
            return ans
        return -1




so = Solution()
print(so.minimumSubarrayLength(nums = [1,2], k = 0))
print(so.minimumSubarrayLength(nums = [1,2,3], k = 2))
print(so.minimumSubarrayLength(nums = [2,1,8], k = 10))




