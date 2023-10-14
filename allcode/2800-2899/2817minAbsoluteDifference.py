

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        n = len(nums)
        def find(l):
            res = inf
            left = []
            for i in range(x, n):
                insort_left(left, l[i - x])
                # if i + 1 - len(left) < x: continue
                p1 = bisect_left(left, l[i])
                if p1 >= len(left):
                    res = min(res, abs(l[i] - left[-1]))
                else:
                    res = min(res, abs(l[i] - left[p1]), abs(l[i] - left[p1 - 1]))
            return res

        r1, r2 = find(nums), find(nums[::-1])
        return min(r1, r2)



so = Solution()
print(so.minAbsoluteDifference(nums = [5,3,2,10,15], x = 1))
print(so.minAbsoluteDifference(nums = [4,3,2,4], x = 2))
print(so.minAbsoluteDifference(nums = [1,2,3,4], x = 3))




