

from leetcode.allcode.competition.mypackage import *

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig = set((x, y) for x, y in dig)
        ans = 0
        for r1, c1, r2, c2 in artifacts:
            flg = True
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if (i, j) not in dig:
                        flg = False
                if not flg:
                    break
            if flg:
                ans += 1
        return ans


so = Solution()
print(so.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]))




