# 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
#
# 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
#
# 例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
# 再例如，[1, 1, 2, 5, 7] 不是等差序列。
# 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
#
# 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
# 题目数据保证答案是一个 32-bit 整数。
#
#
#
# 示例 1：
#
# 输入：nums = [2,4,6,8,10]
# 输出：7
# 解释：所有的等差子序列为：
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
# 示例 2：
#
# 输入：nums = [7,7,7,7,7]
# 输出：16
# 解释：数组中的任意子序列都是等差子序列。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfArithmeticSlices1(self, nums: List[int]) -> int:  # 这个方法可行，但稍有些复杂，没有必要单独考虑相等的数列，看下个方法
        N = len(nums)
        if N < 3:
            return 0
        # 定义两个序列
        seq1 = [0] * N  # 记录以每个 nums[i] 结尾的等差数列 所有公差对应等差数列个数的字典
        seq2 = [0] * N  # 记录非等差数列的情况，以每个 nums[i] 结尾的 “公差”集合，实际就是两个元素的差
        seq1[0], seq1[1] = {}, {}
        seq2[0], seq2[1] = {}, {nums[1] - nums[0]: 1}
        zero = defaultdict(int)
        zero[nums[0]] += 1
        zero[nums[1]] += 1

        for i in range(2, N):
            seq1[i], seq2[i] = defaultdict(int), defaultdict(int)
            zero[nums[i]] += 1
            for j in range(i):
                delta = nums[i] - nums[j]
                if 0 == delta:
                    continue
                seq2[i][delta] += 1
                if delta in seq1[j]:
                    seq1[i][delta] += (seq1[j][delta] + seq2[j][delta])
                elif delta in seq2[j]:
                    seq1[i][delta] += seq2[j][delta]

        print('seq1: ', seq1)
        print('seq2: ', seq2)
        print('zero: ', zero)
        ret = sum([sum(seq1[i].values()) for i in range(N)])
        for e in zero.values():
            ret += (2 ** e - (1 + e + e * (e - 1) // 2))
        return ret

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return 0
        # 定义两个序列
        seq1 = [0] * N  # 记录以每个 nums[i] 结尾的等差数列 所有公差对应等差数列个数的字典，公差: 个数
        seq2 = [0] * N  # 以每个 nums[i] 结尾的两个元素差值字典，差值: 个数
        seq1[0], seq1[1] = {}, {}
        seq2[0], seq2[1] = {}, {nums[1] - nums[0]: 1}

        for i in range(2, N):
            seq1[i], seq2[i] = defaultdict(int), defaultdict(int)
            for j in range(i):
                delta = nums[i] - nums[j]
                seq2[i][delta] += 1
                if delta in seq1[j]:
                    seq1[i][delta] += (seq1[j][delta] + seq2[j][delta])
                elif delta in seq2[j]:
                    seq1[i][delta] += seq2[j][delta]

        print('seq1: ', seq1)
        print('seq2: ', seq2)
        ret = sum([sum(seq1[i].values()) for i in range(N)])
        return ret

so = Solution()
print(so.numberOfArithmeticSlices([2,4,6,8,10]))
print(so.numberOfArithmeticSlices([2,2,3,3,4,5]))
print(so.numberOfArithmeticSlices([79,20,64,28,67,81,60,58,97,85,92,96,82,89,46,50,15,2,36,44,54,2,90,37,7,79,26,40,34,67,64,28,60,89,46,31,9,95,43,19,47,64,48,95,80,31,47,19,72,99,28,46,13,9,64,4,68,74,50,28,69,94,93,3,80,78,23,80,43,49,77,18,68,28,13,61,34,44,80,70,55,85,0,37,93,40,47,47,45,23,26,74,45,67,34,20,33,71,48,96]))
print(so.numberOfArithmeticSlices([2,2,3,4]))
print(so.numberOfArithmeticSlices([7,7,7,7,7]))


