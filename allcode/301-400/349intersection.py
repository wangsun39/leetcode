# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 示例 2：
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
#
# 说明：
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s = s1 | s2
        return list(s)




so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.topKFrequent([1,1,1,2,2,3], 2))




