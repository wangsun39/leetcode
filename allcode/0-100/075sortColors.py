# 给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
#
#
#
# 进阶：
#
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[0]
# 示例 4：
#
# 输入：nums = [1]
# 输出：[1]
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2


from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i, j, k = 0, N - 1, 0   # 下标小于 k 的元素都是 0, 下标大于 k 的元素都是2
        while k < N and j >= 0 and k <= j and i <= j:
            if 0 == nums[k]:
                k += 1
                continue
            if 2 == nums[j]:
                j -= 1
                continue
            if i < k:
                i = k
            if 0 == nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif 2 == nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1

        print(nums)
        return


so = Solution()
print(so.sortColors([2,0,2,1,1,0]))
print(so.sortColors([0, 2]))
print(so.sortColors([0]))
print(so.sortColors([1,2,2,2,2,0,0,0,1,1]))

