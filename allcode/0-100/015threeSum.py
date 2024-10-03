# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
# 提示：
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from leetcode.allcode.competition.mypackage import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counter = Counter(nums)
        nums1, nums2 = [], []
        zero = counter[0]
        for x in counter.keys():
            if x < 0:
                nums1.append(x)
            elif x > 0:
                nums2.append(x)
        ans = []
        if zero >= 3:
            ans.append([0,0,0])
        def f(l1, l2):  # 枚举 l1 中的元素对，到l2中查找
            n1, n2 = len(l1), len(l2)
            s = set(l2)
            for i in range(n1):
                for j in range(i + 1, n1):
                    if -(l1[i] + l1[j]) in s:
                        ans.append([l1[i], l1[j], -(l1[i] + l1[j])])
                if zero and l1[i] < 0 and -l1[i] in s:
                    ans.append([l1[i], 0, -l1[i]])
                if counter[l1[i]] > 1 and -2 * l1[i] in s:
                    ans.append([l1[i], l1[i], -2 * l1[i]])

        f(nums1, nums2)
        f(nums2, nums1)
        # print(sorted(ans))
        return ans




so = Solution()
print(so.threeSum(nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))
print(so.threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(so.threeSum(nums = [-1,-1,-1,1]))
print(so.threeSum(nums = [-1,0,1]))
print(so.threeSum(nums = [-1,0,1,2,-1,-4]))
print(so.threeSum(nums = [0,1,1]))
print(so.threeSum(nums = [0,0,0]))
