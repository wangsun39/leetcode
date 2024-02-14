# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
# 如果可以，请返回 true；否则，返回 false。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
# 示例 2：
#
# 输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
# 示例 3：
#
# 输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
# 示例 4：
#
# 输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
#
#
# 提示：
#
# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 109
#
#
# 注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        sd = SortedDict()
        for kk, v in counter.items():
            sd[kk] = v
        while sd:
            x = sd.keys()[0]
            v = sd[x]
            for i in range(k):
                if x + i not in sd or sd[x + i] < v:
                    return False
                sd[x + i] -= v
                if sd[x + i] == 0:
                    sd.pop(x + i)
        return True


so = Solution()
print(so.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
print(so.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
print(so.isPossibleDivide(nums = [3,3,2,2,1,1], k = 3))
print(so.isPossibleDivide(nums = [1,2,3,4], k = 3))




