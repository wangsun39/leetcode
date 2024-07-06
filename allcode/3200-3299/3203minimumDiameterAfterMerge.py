

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g1 = defaultdict(list)
        for x, y in edges1:
            g1[x].append(y)
            g1[y].append(x)
        g2 = defaultdict(list)
        for x, y in edges2:
            g2[x].append(y)
            g2[y].append(x)

        def diameter(g):
            dq1 = deque([x for x in g if len(g[x]) == 1])
            deg = {k: len(v) for k, v in g.items()}
            cnt = 0
            while dq1:
                dq2 = deque()
                while dq1:
                    x = dq1.popleft()
                    deg[x] -= 1
                    for y in g[x]:
                        if deg[y]:
                            deg[y] -= 1
                            if deg[y] == 1:
                                dq2.append(y)
                cnt += 1
                dq1 = dq2
                if len(dq2) == 1:
                    return cnt * 2
            return cnt * 2 - 1
        diam1, diam2 = diameter(g1), diameter(g2)
        return max(diam1, diam2, (diam1 + 1) // 2 + (diam2 + 1) // 2 + 1)




so = Solution()
print(so.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]))
print(so.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]))




