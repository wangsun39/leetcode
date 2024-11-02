# 给你一个下标从 0 开始的整数数组 mapping ，它表示一个十进制数的映射规则，mapping[i] = j 表示这个规则下将数位 i 映射为数位 j 。
#
# 一个整数 映射后的值 为将原数字每一个数位 i （0 <= i <= 9）映射为 mapping[i] 。
#
# 另外给你一个整数数组 nums ，请你将数组 nums 中每个数按照它们映射后对应数字非递减顺序排序后返回。
#
# 注意：
#
# 如果两个数字映射后对应的数字大小相同，则将它们按照输入中的 相对顺序 排序。
# nums 中的元素只有在排序的时候需要按照映射后的值进行比较，返回的值应该是输入的元素本身。
#
#
# 示例 1：
#
# 输入：mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
# 输出：[338,38,991]
# 解释：
# 将数字 991 按照如下规则映射：
# 1. mapping[9] = 6 ，所有数位 9 都会变成 6 。
# 2. mapping[1] = 9 ，所有数位 1 都会变成 9 。
# 所以，991 映射的值为 669 。
# 338 映射为 007 ，去掉前导 0 后得到 7 。
# 38 映射为 07 ，去掉前导 0 后得到 7 。
# 由于 338 和 38 映射后的值相同，所以它们的前后顺序保留原数组中的相对位置关系，338 在 38 的前面。
# 所以，排序后的数组为 [338,38,991] 。
# 示例 2：
#
# 输入：mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
# 输出：[123,456,789]
# 解释：789 映射为 789 ，456 映射为 456 ，123 映射为 123 。所以排序后数组为 [123,456,789] 。
#
#
# 提示：
#
# mapping.length == 10
# 0 <= mapping[i] <= 9
# mapping[i] 的值 互不相同 。
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] < 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map(x):
            if x == 0: return mapping[0]
            res = 0
            cnt = 0
            while x:
                res += (mapping[x % 10]) * (10 ** cnt)
                x //= 10
                cnt += 1
            return res
        nums2 = [map(x) for x in nums]
        z = list(zip(nums, nums2))
        z.sort(key=lambda x: x[1])
        return [x[0] for x in z]



so = Solution()
print(so.sortJumbled([9,8,7,6,5,4,3,2,1,0], [0,1,2,3,4,5,6,7,8,9]))
print(so.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))
print(so.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]))




