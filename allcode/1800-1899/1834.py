

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks1 = [[x, y, i] for i, [x, y] in enumerate(tasks)]
        tasks1.sort()
        tasks1 = deque(tasks1)
        cur = -inf  # 当前时间
        ans = []
        cand = []
        while tasks1:
            if cur < tasks1[0][0] and not cand:
                cur = tasks1[0][0]
            while tasks1 and cur >= tasks1[0][0]:
                st, t, idx = tasks1.popleft()
                heappush(cand, [t, idx])
            t, i = heappop(cand)
            ans.append(i)
            cur += t
        while cand:
            ans.append(heappop(cand)[1])
        return ans


so = Solution()
print(so.getOrder([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]))
print(so.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(so.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))




