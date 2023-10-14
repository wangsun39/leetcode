
from leetcode.allcode.competition.mypackage import *

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if arr[i] & 1 == arr[i + 1] & 1 == arr[i + 2] & 1 == 1:
                return True
        return False


so = Solution()
print(so.threeConsecutiveOdds([2,6,4,1]))
print(so.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))




