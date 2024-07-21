

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        v2 = reduce(lambda x, y: x ^ y, arr2)
        u = [x & v2 for x in arr1]
        return reduce(lambda x, y: x ^ y, u)


so = Solution()
print(so.getXORSum(arr1 = [1,2,3], arr2 = [6,5]))
print(so.getXORSum(arr1 = [12], arr2 = [4]))




