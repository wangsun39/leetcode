# 给你一个整数数组 nums ，返回出现最频繁的偶数元素。
#
# 如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。
#
# 
#
# 示例 1：
#
# 输入：nums = [0,1,2,2,4,4,1]
# 输出：2
# 解释：
# 数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
# 返回最小的那个，即返回 2 。
# 示例 2：
#
# 输入：nums = [4,4,4,9,2,4]
# 输出：4
# 解释：4 是出现最频繁的偶数元素。
# 示例 3：
#
# 输入：nums = [29,47,21,41,13,37,25,7]
# 输出：-1
# 解释：不存在偶数元素。
# 
#
# 提示：
#
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 105


from leetcode.allcode.competition.mypackage import *

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        me = 0
        ans = 1e6
        for k in counter:
            if k % 2 == 0:
                if counter[k] > me:
                    ans = k
                    me = counter[k]
                elif counter[k] == me:
                    ans = min(k, ans)
        return -1 if ans > 1e5 else ans




so = Solution()
print(so.mostFrequentEven([0,1,2,2,4,4,1]))
print(so.mostFrequentEven([4,4,4,9,2,4]))
print(so.mostFrequentEven([29,47,21,41,13,37,25,7]))




