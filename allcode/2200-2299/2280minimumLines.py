
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x:x[0])
        n = len(stockPrices)
        if n <= 2:
            return n - 1
        start, cur = 0, 2
        ans = 1
        print(stockPrices)
        def equal(A, B, C):
            return (B[1] - A[1]) * (C[0] - B[0]) == (C[1] - B[1]) * (B[0] - A[0])
        while cur < n:
            if equal(stockPrices[start], stockPrices[start + 1], stockPrices[cur]):
                cur += 1
                continue
            start = cur - 1
            cur = cur + 1
            ans += 1
        return ans


so = Solution()
print(so.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
print(so.minimumLines([[3,4],[1,2],[7,8],[2,3]]))




