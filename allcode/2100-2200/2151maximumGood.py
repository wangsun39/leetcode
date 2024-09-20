

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        def check(num):
            for i in range(n):
                for j in range(n):
                    if statements[i][j] == 2: continue
                    if num & (1 << i):
                        if bool(statements[i][j]) != bool(num & (1 << j)):
                            return False
            return True
        for i in range(1 << n):
            if check(i):
                ans = max(ans, i.bit_count())

        return ans


so = Solution()
print(so.maximumGood(statements = [[2,1,1,2,2,2,1,1,2,2],[2,2,1,1,2,1,1,1,1,2],[1,2,2,2,1,1,1,1,1,1],[1,1,1,2,1,2,2,2,1,2],[1,1,1,1,2,1,1,1,1,1],[2,1,1,1,1,2,1,1,1,2],[1,2,1,1,1,2,2,1,1,1],[1,1,1,2,2,2,1,2,1,1],[1,1,2,1,2,1,1,1,2,1],[2,1,1,1,1,1,1,1,1,2]]))
print(so.maximumGood(statements = [[2,0],[0,2]] ))
print(so.maximumGood(statements = [[2,1,2],[1,2,2],[2,0,2]]))




