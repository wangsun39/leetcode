

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for x, y in pairs:
            g[x].append(y)
            g[y].append(x)

        start = pairs[0][0]
        for k, v in g.items():
            if v & 1:
                start = k
                break




so = Solution()
print(so.validArrangement(root, 3, 6))




