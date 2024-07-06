

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(r, b):
            for i in range(max(r, b) + 1):
                if i & 1 == 0:
                    if r < i + 1:
                        return i
                    r -= (i + 1)
                else:
                    if b < i + 1:
                        return i
                    b -= (i + 1)
        return max(check(red, blue), check(blue, red))


so = Solution()
print(so.maxHeightOfTriangle(red = 2, blue = 1))
print(so.maxHeightOfTriangle(red = 2, blue = 4))
print(so.maxHeightOfTriangle(red = 1, blue = 1))




