# 给你两个整数数组 nums1 和 nums2 ，它们长度都为 n 。
#
# 两个数组的 异或值之和 为 (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) （下标从 0 开始）。
#
# 比方说，[1,2,3] 和 [3,2,1] 的 异或值之和 等于 (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4 。
# 请你将 nums2 中的元素重新排列，使得 异或值之和 最小 。
#
# 请你返回重新排列之后的 异或值之和 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2], nums2 = [2,3]
# 输出：2
# 解释：将 nums2 重新排列得到 [3,2] 。
# 异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2 。
# 示例 2：
#
# 输入：nums1 = [1,0,3], nums2 = [5,3,4]
# 输出：8
# 解释：将 nums2 重新排列得到 [5,4,3] 。
# 异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8 。
#
#
# 提示：
#
# n == nums1.length
# n == nums2.length
# 1 <= n <= 14
# 0 <= nums1[i], nums2[i] <= 107

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        @cache
        def dfs(tu1, tu2):
            if len(tu1) == 0:
                return 0
            if tu1[0] == 0 or tu2[0] == 0:
                return sum(tu1[i] ^ tu2[i] for i in range(len(tu1)))
            if len(tu1) == 1:
                return tu1[0] ^ tu2[0]
            bl1, bl2 = tu1[0].bit_length(), tu2[0].bit_length()
            len1 = sum(x.bit_length() == bl1 for x in tu1)
            len2 = sum(x.bit_length() == bl2 for x in tu2)
            res = inf
            if bl1 == bl2:   # 长度相同的可以任意组合进行枚举
                for i in range(len1):
                    for j in range(len2):
                        li1, li2 = list(tu1), list(tu2)
                        li1[0], li1[i] = li1[i], li1[0]
                        li2[0], li2[j] = li2[j], li2[0]
                        li1[0] &= ~(1 << (bl1 - 1))  # 同时去掉最高位
                        li2[0] &= ~(1 << (bl2 - 1))
                        li1.sort(reverse=True)
                        li2.sort(reverse=True)
                        res = min(res, li1[0] ^ li2[0] + dfs(tuple(li1[1:]), tuple(li2[1:])))
            else:
                if bl1 < bl2:
                    bl1, bl2 = bl2, bl1
                    tu1, tu2 = tu2, tu1
                    len1, len2 = len2, len1
                base = (1 << (bl1 - 1)) * len1  # 这些高位都会保留在最终的和中
                tu1 = tuple(sorted([tu1[i] & ~(1 << (bl1 - 1)) for i in range(len(tu1))], reverse=True))  # 剩下只要考虑最高位是len1-1的情况
                return dfs(tu1, tu2) + base
            return res
        return dfs(tuple(nums1), tuple(nums2))




so = Solution()
print(so.minimumXORSum(nums1 = [1,0,3], nums2 = [5,3,4]))  # 8
print(so.minimumXORSum(nums1 = [1,2], nums2 = [2,3]))




