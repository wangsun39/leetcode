# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 你可以假设所有输入数组都可以得到满足题目要求的结果。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,5,1,1,6,4]
# 输出：[1,6,1,5,1,4]
# 解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
# 示例 2：
#
# 输入：nums = [1,3,2,2,3,1]
# 输出：[2,3,1,3,1,2]
#  
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5000
# 题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
#  
#
# 进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？


from leetcode.allcode.competition.mypackage import *
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        N = len(nums)
        nums.sort()
        if N % 2 == 0:
            mid = N // 2  # 中位数
            left, right = nums[:mid], nums[mid:]
            for i in range(mid):
                nums[i*2] = left[mid-i-1]
                nums[i*2+1] = right[mid-i-1]
        else:
            mid = N // 2  # 中位数
            tmp = nums[mid]
            left, right = nums[:mid], nums[mid+1:]
            for i in range(mid):
                nums[i*2] = left[i]
                nums[i*2+1] = right[i]
            nums[N - 1] = tmp
        print(nums)
        return

    def wiggleSort1(self, nums: List[int]) -> None:
        # 2024/4/27 排序，性能略低
        counter = Counter(nums)

        n = len(nums)
        v, c = counter.most_common(1)[0]  # 众数
        # c 必然<= n/2
        if c * 2 < n or n & 1:
            # 按排序交叉保存即可
            s_nums = sorted(nums)
            for i in range((n + 1) // 2):
                nums[i * 2] = s_nums[i]
            for i in range(n // 2):
                nums[i * 2 + 1] = s_nums[(n + 1) // 2 + i]
            return

        # 剩下就是c == n//2的情况
        less = [x for x in nums if x < v]
        more = [x for x in nums if x > v]
        if len(more) == 0:
            # 众数是最大值，把众数放在偶数位置
            for i in range(n // 2):
                nums[i * 2] = less[i]
                nums[i * 2 + 1] = v
            return
        for i in range(len(more)):
            nums[i * 2] = v
            nums[i * 2 + 1] = more[i]
        for i in range(len(more), n // 2):
            nums[i * 2] = less[i - len(more)]
            nums[i * 2 + 1] = v


so = Solution()
print('res =', so.wiggleSort([1,5,1,1,6,4]))
print('res =', so.wiggleSort([4,5,5,6]))


