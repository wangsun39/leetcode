from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if 1 == N:
            return 1
        trustCount = set()  # 信任别人的集合
        trustedCount = defaultdict(int)  # 被信任的字典，与trustCount互斥
        for t in trust:
            if t[0] in trustedCount:
                del trustedCount[t[0]]
            if t[1] not in trustCount:
                trustedCount[t[1]] += 1
            trustCount.add(t[0])
        if len(trustedCount) == 1 and list(trustedCount.values())[0] == N-1:
            return list(trustedCount.keys())[0]
        return -1




so = Solution()
print(so.findJudge(1, []))
print(so.findJudge(2, [[1,2]]))
print(so.findJudge(3, [[1,3],[2,3]]))
print(so.findJudge(3, [[1,3],[2,3],[3,1]]))
print(so.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

