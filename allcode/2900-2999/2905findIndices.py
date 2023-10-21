

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
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


so = Solution()
print(so.findIndices(nums = [5,10], indexDifference = 1, valueDifference = 2))
print(so.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
print(so.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))
print(so.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))




