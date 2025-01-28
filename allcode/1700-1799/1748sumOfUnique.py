# 给你一个整数数组nums。数组中唯一元素是那些只出现恰好一次的元素。
#
# 请你返回 nums中唯一元素的 和。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,2]
# 输出：4
# 解释：唯一元素为 [1,3] ，和为 4 。
# 示例 2：
#
# 输入：nums = [1,1,1,1,1]
# 输出：0
# 解释：没有唯一元素，和为 0 。
# 示例 3 ：
#
# 输入：nums = [1,2,3,4,5]
# 输出：15
# 解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100



from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique, multi = set(), set()
        for e in nums:
            if e in unique:
                unique.remove(e)
                multi.add(e)
            elif e in multi:
                continue
            else:
                unique.add(e)
        return sum(unique)


so = Solution()

print(so.sumOfUnique([1,2,3,2]))
print(so.sumOfUnique([1,1,1,1,1]))




