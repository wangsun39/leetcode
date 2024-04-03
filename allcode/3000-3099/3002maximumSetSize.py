# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们的长度都是偶数 n 。
#
# 你必须从 nums1 中移除 n / 2 个元素，同时从 nums2 中也移除 n / 2 个元素。移除之后，你将 nums1 和 nums2 中剩下的元素插入到集合 s 中。
#
# 返回集合 s可能的 最多 包含多少元素。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,1,2], nums2 = [1,1,1,1]
# 输出：2
# 解释：从 nums1 和 nums2 中移除两个 1 。移除后，数组变为 nums1 = [2,2] 和 nums2 = [1,1] 。因此，s = {1,2} 。
# 可以证明，在移除之后，集合 s 最多可以包含 2 个元素。
# 示例 2：
#
# 输入：nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]
# 输出：5
# 解释：从 nums1 中移除 2、3 和 6 ，同时从 nums2 中移除两个 3 和一个 2 。移除后，数组变为 nums1 = [1,4,5] 和 nums2 = [2,3,2] 。因此，s = {1,2,3,4,5} 。
# 可以证明，在移除之后，集合 s 最多可以包含 5 个元素。
# 示例 3：
#
# 输入：nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]
# 输出：6
# 解释：从 nums1 中移除 1、2 和 3 ，同时从 nums2 中移除 4、5 和 6 。移除后，数组变为 nums1 = [1,2,3] 和 nums2 = [4,5,6] 。因此，s = {1,2,3,4,5,6} 。
# 可以证明，在移除之后，集合 s 最多可以包含 6 个元素。
#
#
# 提示：
#
# n == nums1.length == nums2.length
# 1 <= n <= 2 * 104
# n是偶数。
# 1 <= nums1[i], nums2[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        s = s1 & s2
        ans1 = set()
        for x in s1:
            if x not in s2:
                ans1.add(x)
            if len(ans1) >= n // 2:
                break
        ans2 = set()
        for x in s2:
            if x not in s1:
                ans2.add(x)
            if len(ans2) >= n // 2:
                break
        ans = ans1 | ans2
        for x in s:
            if len(ans) >= n:
                break
            ans.add(x)
        return len(ans)




so = Solution()
print(so.maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))
print(so.maximumSetSize(nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]))
print(so.maximumSetSize(nums1 = [1,2,1,2], nums2 = [1,1,1,1]))




