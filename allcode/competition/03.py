

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        rmv = SortedList()
        ans = []
        cur = n - 1
        for x, y in queries:
            if len(rmv) == 0 or x > rmv[-1][1]:
                rmv.add([x, y])
                cur -= (y - x - 1)
                ans.append(cur)
                continue
            p = rmv.bisect_right([x, y])
            if p == 0:
                if rmv[0][0] == x and rmv[0][1] >= y:
                    ans.append(cur)
                    continue
                if rmv[0][0] >= y:
                    rmv.add([x, y])
                    cur -= (y - x - 1)
                    ans.append(cur)
                    continue
            elif rmv[p - 1][1] >= y:
                ans.append(cur)
                continue
            elif rmv[p - 1][0] == x:
                p = p - 1
            # 剩下的情况，就是 [x,y] 包含已有的区间，需要合并掉
            dis0 = 0  # 之前减少的长度
            while p < len(rmv) and rmv[p][1] <= y:
                dis0 += (rmv[p][1] - rmv[p][0] - 1)
                del(rmv[p])
            dis1 = y - x - 1  # 现在减少的长度
            rmv.add([x, y])
            cur -= (dis1 - dis0)
            ans.append(cur)
        return ans


so = Solution()
print(so.shortestDistanceAfterQueries( n = 6, queries = [[3,5],[2,5]]))  # [4,3]
print(so.shortestDistanceAfterQueries( n = 5, queries = [[1,4],[2,4]]))  # [2,2]
print(so.shortestDistanceAfterQueries( n = 5, queries = [[2, 4], [0, 2], [0, 4]]))
print(so.shortestDistanceAfterQueries( n = 4, queries = [[0, 3], [0, 2]]))




