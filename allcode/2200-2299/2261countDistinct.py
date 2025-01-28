# 给你一个整数数组 nums 和两个整数 k 和 p ，找出并返回满足要求的不同的子数组数，要求子数组中最多 k 个可被 p 整除的元素。
#
# 如果满足下述条件之一，则认为数组 nums1 和 nums2 是 不同 数组：
#
# 两数组长度 不同 ，或者
# 存在 至少 一个下标 i 满足 nums1[i] != nums2[i] 。
# 子数组 定义为：数组中的连续元素组成的一个 非空 序列。
#
# 
#
# 示例 1：
#
# 输入：nums = [2,3,3,2,2], k = 2, p = 2
# 输出：11
# 解释：
# 位于下标 0、3 和 4 的元素都可以被 p = 2 整除。
# 共计 11 个不同子数组都满足最多含 k = 2 个可以被 2 整除的元素：
# [2]、[2,3]、[2,3,3]、[2,3,3,2]、[3]、[3,3]、[3,3,2]、[3,3,2,2]、[3,2]、[3,2,2] 和 [2,2] 。
# 注意，尽管子数组 [2] 和 [3] 在 nums 中出现不止一次，但统计时只计数一次。
# 子数组 [2,3,3,2,2] 不满足条件，因为其中有 3 个元素可以被 2 整除。
# 示例 2：
#
# 输入：nums = [1,2,3,4], k = 4, p = 1
# 输出：10
# 解释：
# nums 中的所有元素都可以被 p = 1 整除。
# 此外，nums 中的每个子数组都满足最多 4 个元素可以被 1 整除。
# 因为所有子数组互不相同，因此满足所有限制条件的子数组总数为 10 。
# 
#
# 提示：
#
# 1 <= nums.length <= 200
# 1 <= nums[i], p <= 200
# 1 <= k <= nums.length






from leetcode.allcode.competition.mypackage import *
class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        idx = []
        N = len(nums)
        for i in range(N):
            if nums[i] % p == 0:
                idx.append(i)

        # @lru_cache(None)
        def handleSection(i, j):
            nonlocal subArrs
            n = (j - i + 1)
            for k in range(n):
                for t in range(k, n):
                    if tuple(nums[i + k: i + t + 1]) not in subArrs:
                        subArrs.add(tuple(nums[i + k: i + t + 1]))
            return

        subArrs = set()
        if len(idx) == 0:
            handleSection(0, N - 1)
            return len(subArrs)
        # idx[0] = 0
        idx.append(N)

        if len(idx) <= k:
            handleSection(0, N - 1)
        else:
            for i in range(len(idx) - k):
                if i == 0:
                    handleSection(0, idx[i + k] - 1)
                else:
                    handleSection(idx[i - 1] + 1, idx[i + k] - 1)
        return len(subArrs)


so = Solution()
print(so.countDistinct(
    [17, 88, 83, 119, 79, 92, 135, 77, 140, 15, 80, 10, 26, 188, 5, 161, 15, 52, 179, 118, 58, 171, 188, 75, 161, 39,
     96, 160, 85, 118, 162, 18, 154, 165, 76, 126, 155, 157, 51, 42, 112, 6, 100, 142, 149, 33, 76, 20, 63, 128, 188,
     133, 71, 190, 61, 12, 164, 22, 64, 183, 2, 61, 149, 47, 156, 32, 67, 144, 21, 194, 112, 74, 55, 47, 183, 32, 32, 6,
     10, 64, 17, 182, 17, 141, 57, 168, 157, 9, 77, 107, 144, 69, 150, 42, 158, 31, 185, 200, 21, 141, 66, 17, 157, 175,
     95, 200, 129, 75, 189, 151, 145, 12, 78, 29, 148, 33, 200, 29, 168, 138, 62, 29, 87, 87, 119, 175, 170, 25, 136,
     50, 189, 25, 127, 116, 91, 19, 168, 65, 46, 34, 39, 3, 28, 193, 25, 83, 126, 102, 184, 137, 95, 91, 151, 174, 155,
     52, 195, 94, 165, 191, 30, 64, 62, 82, 172, 89, 109], k=1, p=25))

print(so.countDistinct(
    [64, 37, 33, 5, 13, 47, 35, 3, 67, 26, 50, 44, 55, 7, 62, 10, 16, 45, 27, 68, 69, 93, 49, 67, 21, 64, 97, 88, 51,
     23, 62, 31, 76, 57, 69, 52, 70, 32, 55, 14, 92, 50, 41, 9, 98, 50, 82, 14, 31, 85, 89, 80, 96, 62, 10, 19, 47, 40,
     25, 27, 49, 40, 72, 18, 12, 21, 53, 94, 69, 90, 6, 93, 47, 14, 18, 81, 73, 60, 36, 2, 62, 14, 7, 95, 96, 16, 40, 9,
     72, 50, 40, 14, 67, 51, 30, 31, 82, 35, 70, 14, 22, 53, 11, 13, 67, 90, 16, 46, 70, 6, 79, 31, 94, 52, 62, 65, 1,
     32, 51, 2, 27, 64, 42, 11, 55, 61, 45, 55, 11, 1, 34, 86, 84, 21, 58, 40, 76, 45, 68, 17, 75, 79, 96, 78, 80, 31,
     59, 63, 78], k=91, p=11))
print(so.countDistinct([6, 20, 5, 18], k=3, p=14))
print(so.countDistinct([2, 3, 3, 2, 2], k=2, p=2))
print(so.countDistinct([1, 2, 3, 4], k=4, p=1))


