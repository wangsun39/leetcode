# 给你一个下标从 0 开始的整数数组 nums 。
#
# 一开始，所有下标都没有被标记。你可以执行以下操作任意次：
#
# 选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
# 请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
#
#
#
# 示例 1：
#
# 输入：nums = [3,5,2,4]
# 输出：2
# 解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
# 没有其他更多可执行的操作，所以答案为 2 。
# 示例 2：
#
# 输入：nums = [9,2,5,4]
# 输出：4
# 解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
# 第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
# 没有其他更多可执行的操作，所以答案为 4 。
# 示例 3：
#
# 输入：nums = [7,6,8]
# 输出：0
# 解释：没有任何可以执行的操作，所以答案为 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        cur = n // 2
        left = deque(nums[cur:])
        for i in range(n // 2):
            while len(left) and left[0] < nums[i] * 2:
                left.popleft()
            if len(left):
                # print(nums[i], left[0])
                ans += 2
                left.popleft()
            else:
                break
        return ans




so = Solution()
print(so.maxNumOfMarkedIndices([72,97,60,79,68,25,63,82,88,60,37,60,44,14,62,36,52,73,26,98,86,50,74,68,53,80,90,60,78,56,53,84,2]))  # 14
print(so.maxNumOfMarkedIndices([1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]))  # 64
print(so.maxNumOfMarkedIndices([3,5,2,4]))  # 2
print(so.maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))  # 26
print(so.maxNumOfMarkedIndices([9,2,5,4]))  # 4
print(so.maxNumOfMarkedIndices([7,6,8]))




