# 给你一个整数数组 nums ，数组中的元素都是 正 整数。定义一个加密函数 encrypt ，encrypt(x) 将一个整数 x 中 每一个 数位都用 x 中的 最大 数位替换。比方说 encrypt(523) = 555 且 encrypt(213) = 333 。
#
# 请你返回数组中所有元素加密后的 和 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
#
# 输出：6
#
# 解释：加密后的元素位 [1,2,3] 。加密元素的和为 1 + 2 + 3 == 6 。
#
# 示例 2：
#
# 输入：nums = [10,21,31]
#
# 输出：66
#
# 解释：加密后的元素为 [11,22,33] 。加密元素的和为 11 + 22 + 33 == 66 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            s = str(x)
            l = list(s)
            mx = max(l)
            ans += int(''.join([mx] * len(l)))
        return ans



so = Solution()
print(so.sumOfEncryptedInt([1,2,3]))
print(so.sumOfEncryptedInt([10,21,31]))




