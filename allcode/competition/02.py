

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x

        x -= 1
        y -= 1
        f = [[inf] * n for _ in range(n)]  # f[i][j] 表示 i 到 j 的最小距离
        for i in range(n):
            for j in range(i + 1, n):
                f[i][j] = j - i
                if i <= x <= j:
                    f[i][j] = min(f[i][j], x - i + 1 + abs(y - j))
                if x < i:
                    f[i][j] = min(f[i][j], i - x + 1 + abs(y - j))

        ans = [0] * n
        for j in range(n):
            for t in range(j + 1, n):
                k = f[j][t]
                ans[k - 1] += 2

        return ans




so = Solution()
print(so.countOfPairs(n = 3, x = 1, y = 3))




