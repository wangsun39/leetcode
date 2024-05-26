# 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。
#
# 你的任务是从范围 [0, n - 1] 内找出  2 个满足下述所有条件的下标 i 和 j ：
#
# abs(i - j) >= indexDifference 且
# abs(nums[i] - nums[j]) >= valueDifference
# 返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] ；否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。
#
# 注意：i 和 j 可能 相等 。
#
#
#
# 示例 1：
#
# 输入：nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
# 输出：[0,3]
# 解释：在示例中，可以选择 i = 0 和 j = 3 。
# abs(0 - 3) >= 2 且 abs(nums[0] - nums[3]) >= 4 。
# 因此，[0,3] 是一个符合题目要求的答案。
# [3,0] 也是符合题目要求的答案。
# 示例 2：
#
# 输入：nums = [2,1], indexDifference = 0, valueDifference = 0
# 输出：[0,0]
# 解释：
# 在示例中，可以选择 i = 0 和 j = 0 。
# abs(0 - 0) >= 0 且 abs(nums[0] - nums[0]) >= 0 。
# 因此，[0,0] 是一个符合题目要求的答案。
# [0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。
# 示例 3：
#
# 输入：nums = [1,2,3], indexDifference = 2, valueDifference = 4
# 输出：[-1,-1]
# 解释：在示例中，可以证明无法找出 2 个满足所有条件的下标。
# 因此，返回 [-1,-1] 。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= indexDifference <= 105
# 0 <= valueDifference <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findIndices1(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        if indexDifference >= n:
            return [-1, -1]
        sl = SortedList((x, i) for i, x in enumerate(nums[indexDifference:], indexDifference))
        for i, x in enumerate(nums):
            t1, t2 = x - valueDifference, x + valueDifference
            p1 = sl.bisect_right((t1, inf))
            if p1 > 0:
                return [sl[p1 - 1][1], i]
            p2 = sl.bisect_left((t2, -inf))
            if p2 < len(sl):
                return [i, sl[p2][1]]
            if i + indexDifference < n:
                sl.remove((nums[i + indexDifference], i + indexDifference))
            if i - indexDifference >= 0:
                sl.add((nums[i - indexDifference], i - indexDifference))
        return [-1, -1]

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 2023/11/11 单调栈，O(n)
        s1 = deque()  # 最大值，单调减的栈
        for i, x in enumerate(nums[indexDifference:], indexDifference):
            while s1 and s1[-1][1] <= x:
                s1.pop()
            s1.append([i, x])
        s2 = deque()  # 最小值，单调增的栈
        for i, x in enumerate(nums[indexDifference:], indexDifference):
            while s2 and s2[-1][1] >= x:
                s2.pop()
            s2.append([i, x])
        for i, x in enumerate(nums):
            while s1 and s1[0][0] - i < indexDifference:
                s1.popleft()
            while s2 and s2[0][0] - i < indexDifference:
                s2.popleft()
            if s1 and s1[0][1] - x >= valueDifference:
                return [i, s1[0][0]]
            if s2 and x - s2[0][1] >= valueDifference:
                return [i, s2[0][0]]
            if not s1 and not s2:
                return [-1, -1]
        return [-1, -1]

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 2024/5/25 双指针 + 维护最大最小值
        n = len(nums)
        mn = mx = nums[0]
        mn_i = mx_i = 0
        for i in range(indexDifference, n):
            x = nums[i]
            if abs(x - mn) >= valueDifference:
                return [mn_i, i]
            if abs(x - mx) >= valueDifference:
                return [mx_i, i]
            j = i - indexDifference + 1
            if j >= n: break
            if nums[j] < mn:
                mn, mn_i = nums[j], j
            if nums[j] > mx:
                mx, mx_i = nums[j], j
        return [-1, -1]

so = Solution()
print(so.findIndices(nums = [5,10], indexDifference = 1, valueDifference = 2))
print(so.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
print(so.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))
print(so.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))




