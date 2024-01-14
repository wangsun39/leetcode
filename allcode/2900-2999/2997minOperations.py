# 给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。
#
# 你可以对数组执行以下操作 任意次 ：
#
# 选择数组里的 任意 一个元素，并将它的 二进制 表示 翻转 一个数位，翻转数位表示将 0 变成 1 或者将 1 变成 0 。
# 你的目标是让数组里 所有 元素的按位异或和得到 k ，请你返回达成这一目标的 最少 操作次数。
#
# 注意，你也可以将一个数的前导 0 翻转。比方说，数字 (101)2 翻转第四个数位，得到 (1101)2 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,3,4], k = 1
# 输出：2
# 解释：我们可以执行以下操作：
# - 选择下标为 2 的元素，也就是 3 == (011)2 ，我们翻转第一个数位得到 (010)2 == 2 。数组变为 [2,1,2,4] 。
# - 选择下标为 0 的元素，也就是 2 == (010)2 ，我们翻转第三个数位得到 (110)2 == 6 。数组变为 [6,1,2,4] 。
# 最终数组的所有元素异或和为 (6 XOR 1 XOR 2 XOR 4) == 1 == k 。
# 无法用少于 2 次操作得到异或和等于 k 。
# 示例 2：
#
# 输入：nums = [2,0,2,0], k = 0
# 输出：0
# 解释：数组所有元素的异或和为 (2 XOR 0 XOR 2 XOR 0) == 0 == k 。所以不需要进行任何操作。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 106
# 0 <= k <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        v = reduce(lambda x, y: x ^ y, nums)
        return (v ^ k).bit_count()


so = Solution()
print(so.minOperations(nums = [2,1,3,4], k = 1))
print(so.minOperations(nums = [2,0,2,0], k = 0))




