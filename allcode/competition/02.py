

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr = ['0', '1']
        for _ in range(n - 1):
            cur = []
            for x in arr:
                if x[-1] == '0':
                    cur.append(x + '1')
                else:
                    cur.append(x + '1')
                    cur.append(x + '0')
            arr = cur
        return arr


so = Solution()
print(so.validStrings(3))




