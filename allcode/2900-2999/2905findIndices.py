

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

so = Solution()
print(so.findIndices(nums = [5,10], indexDifference = 1, valueDifference = 2))
print(so.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
print(so.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))
print(so.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))




