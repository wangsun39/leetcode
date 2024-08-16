

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for i, x in enumerate(arr):
            if x <= pre + 1:
                pre = x
            else:
                pre += 1
        return pre


so = Solution()
print(so.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))
print(so.maximumElementAfterDecrementingAndRearranging([100,1,1000]))
print(so.maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))




