# 给你两个整数 n 和 k。
#
# 最初，你有一个长度为 n 的整数数组 a，对所有 0 <= i <= n - 1，都有 a[i] = 1 。每过一秒，你会同时更新每个元素为其前面所有元素的和加上该元素本身。例如，一秒后，a[0] 保持不变，a[1] 变为 a[0] + a[1]，a[2] 变为 a[0] + a[1] + a[2]，以此类推。
#
# 返回 k 秒后 a[n - 1] 的值。
#
# 由于答案可能非常大，返回其对 109 + 7 取余 后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 5
#
# 输出：56
#
# 解释：
#
# 时间（秒）	数组状态
# 0	[1,1,1,1]
# 1	[1,2,3,4]
# 2	[1,3,6,10]
# 3	[1,4,10,20]
# 4	[1,5,15,35]
# 5	[1,6,21,56]
# 示例 2：
#
# 输入：n = 5, k = 3
#
# 输出：35
#
# 解释：
#
# 时间（秒）	数组状态
# 0	[1,1,1,1,1]
# 1	[1,2,3,4,5]
# 2	[1,3,6,10,15]
# 3	[1,4,10,20,35]
#
#
# 提示：
#
# 1 <= n, k <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        nums = [1] * n
        for i in range(k):
            for j in range(1, n):
                nums[j] += nums[j - 1]
                nums[j] %= MOD
        return nums[-1]


so = Solution()
print(so.valueAfterKSeconds(n = 4, k = 5))
print(so.valueAfterKSeconds(n = 5, k = 3))




