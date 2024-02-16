

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c:
                        ans += 1
        return ans


so = Solution()
print(so.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))




