# 给你一个由 正整数 组成的数组 nums。
#
# 如果一个数组 arr 满足 prod(arr) == lcm(arr) * gcd(arr)，则称其为 乘积等价数组 ，其中：
#
# prod(arr) 表示 arr 中所有元素的乘积。
# gcd(arr) 表示 arr 中所有元素的最大公因数 (GCD)。
# lcm(arr) 表示 arr 中所有元素的最小公倍数 (LCM)。
# 返回数组 nums 的 最长 乘积等价子数组 的长度。
#
# 子数组 是数组中连续的、非空的元素序列。
#
# 术语 gcd(a, b) 表示 a 和 b 的 最大公因数 。
#
# 术语 lcm(a, b) 表示 a 和 b 的 最小公倍数 。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,1,2,1,1,1]
#
# 输出： 5
#
# 解释：
#
# 最长的乘积等价子数组是 [1, 2, 1, 1, 1]，其中 prod([1, 2, 1, 1, 1]) = 2， gcd([1, 2, 1, 1, 1]) = 1，以及 lcm([1, 2, 1, 1, 1]) = 2。
#
# 示例 2：
#
# 输入： nums = [2,3,4,5,6]
#
# 输出： 3
#
# 解释：
#
# 最长的乘积等价子数组是 [3, 4, 5]。
#
# 示例 3：
#
# 输入： nums = [1,2,3,1,4,5,1]
#
# 输出： 5
#
#
#
# 提示：
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        def check(i, j):
            p = lc = gc = nums[i]
            for k in range(i + 1, j + 1):
                p *= nums[k]
                lc = lcm(lc, nums[k])
                gc = gcd(gc, nums[k])
            return p == lc * gc
        for i in range(n):
            for j in range(i, n):
                if j - i + 1 <= ans: continue
                if check(i, j):
                    ans = j - i + 1
        return ans



so = Solution()
print(so.maxLength([1,2,1,2,1,1,1]))




