# 给定两个大小相等的数组nums1和nums2，nums1相对于 nums2 的优势可以用满足nums1[i] > nums2[i]的索引 i的数目来描述。
#
# 返回 nums1的任意排列，使其相对于 nums2的优势最大化。
#
#
#
# 示例 1：
#
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
# 示例 2：
#
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
#
#
# 提示：
#
# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109
#
# https://leetcode.cn/problems/advantage-shuffle


from leetcode.allcode.competition.mypackage import *
import collections
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(reverse=True)
        n = len(nums2)
        n2 = sorted(zip(nums2, range(n)), reverse=True)
        ans = [0] * n
        i, k = 0, n - 1
        for j in range(n):
            e, idx = n2[j]
            if e < nums1[i]:
                ans[idx] = nums1[i]
                i += 1
            else:
                ans[idx] = nums1[k]
                k -= 1
        return ans


so = Solution()
print(so.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))  # [2,11,7,15]
print(so.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))

