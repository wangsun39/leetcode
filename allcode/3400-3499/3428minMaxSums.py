# 给你一个整数数组 nums 和一个正整数 k，返回所有长度最多为 k 的 子序列 中 最大值 与 最小值 之和的总和。
#
# 非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。
#
# 由于答案可能非常大，请返回对 109 + 7 取余数的结果。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,3], k = 2
#
# 输出： 24
#
# 解释：
#
# 数组 nums 中所有长度最多为 2 的子序列如下：
#
# 子序列	最小值	最大值	和
# [1]	1	1	2
# [2]	2	2	4
# [3]	3	3	6
# [1, 2]	1	2	3
# [1, 3]	1	3	4
# [2, 3]	2	3	5
# 总和	 	 	24
# 因此，输出为 24。
#
# 示例 2：
#
# 输入： nums = [5,0,6], k = 1
#
# 输出： 22
#
# 解释：
#
# 对于长度恰好为 1 的子序列，最小值和最大值均为元素本身。因此，总和为 5 + 5 + 0 + 0 + 6 + 6 = 22。
#
# 示例 3：
#
# 输入： nums = [1,1,1], k = 2
#
# 输出： 12
#
# 解释：
#
# 子序列 [1, 1] 和 [1] 各出现 3 次。对于所有这些子序列，最小值和最大值均为 1。因此，总和为 12。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 1 <= k <= min(100, nums.length)

from leetcode.allcode.competition.mypackage import *

MOD = 10 ** 9 + 7
def generate_comb_array(n, m):
    # 初始化二维数组，第一列为1，对角线元素也为1
    comb_array = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        comb_array[i][0] = 1
    for i in range(m + 1):
        comb_array[i][i] = 1

    # 递推计算组合数
    for i in range(1, n + 1):
        for j in range(1, min(i, m) + 1):
            comb_array[i][j] = (comb_array[i - 1][j - 1] + comb_array[i - 1][j]) % MOD
    return comb_array

n = 100000
m = 100
comb_array = generate_comb_array(n, m)
# print(comb_array)

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        for i, x in enumerate(nums):
            larger = n - 1 - i
            for j in range(k): # 选j个>=x的值
                if larger < j: break
                ans += comb_array[larger][j] * x
                ans %= MOD
            less = i
            for j in range(k): # 选j个<=x的值
                if less < j: break
                ans += comb_array[less][j] * x
                ans %= MOD
        return ans


so = Solution()
print(so.minMaxSums(nums = [1,2,3], k = 2))




