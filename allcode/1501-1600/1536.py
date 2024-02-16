

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zero_cnt = [0] * n  # 计算每行最右侧有多个连续0
        for i in range(n):
            c = 0
            for j in range(n - 1, 0, -1):
                if grid[i][j] != 0:
                    break
                else:
                    c += 1
                    zero_cnt[i] = c
        ans = 0
        for i in range(n):
            if zero_cnt[i] < n - i - 1:
                isOk = False
                for j in range(i + 1, n):
                    if zero_cnt[j] >= n - i - 1:
                        ans += j - i
                        zero_cnt[i + 1: j + 1] = zero_cnt[i: j]
                        isOk = True
                        break
                if not isOk:
                    return -1

        return ans


so = Solution()
print(so.minSwaps(grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]))
print(so.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))
print(so.minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(so.minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]))




