# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
#
#  
#
# 进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,0]
# 输出：3
# 示例 2：
#
# 输入：nums = [3,4,-1,1]
# 输出：2
# 示例 3：
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
#  
#
# 提示：
#
# 0 <= nums.length <= 300
# -231 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        if 0 == N:
            return 1
        nums.append(nums[0])  # 在末尾再放一个已有元素，防止所有数组所有元素就是1...N的一个排列
        for i in range(N):
            id1, id2 = i, nums[i]
            while True:
                if id2 == 'exist' or id2 <= 0 or id2 > 300 or id2 >= N + 1:
                    break
                tmp = nums[id2]
                nums[id2] = 'exist'
                id1 = id2
                id2 = tmp
        print(nums)
        for i, e in enumerate(nums[1:]):
            if e != 'exist':
                return i + 1
        return N + 1


so = Solution()

print(so.firstMissingPositive([10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6]))   # 3
print(so.firstMissingPositive([1,2,3]))   # 4
print(so.firstMissingPositive([1,2,0]))   # 3
print(so.firstMissingPositive([3,4,-1,1]))   # 2
print(so.firstMissingPositive([7,8,9,11,12]))   # 1
