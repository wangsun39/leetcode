

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        l1 = list(permutations(nums1))
        l1 = list(set(l1))
        # print(len(l1))
        l_to_idx = {x: i for i, x in enumerate(l1)}
        m = len(l_to_idx)
        g = defaultdict(list)
        for arr in l1:
            for l in range(n):
                for r in range(l, n):
                    la = list(arr)
                    lb = la[:l] + la[r + 1:]
                    for i in range(len(lb) + 1):
                        lc = lb[:i] + la[l: r + 1] + lb[i:]
                        arr2 = tuple(lc)
                        if arr != arr2:
                            g[l_to_idx[arr]].append([l_to_idx[arr2], 1])
                            g[l_to_idx[arr2]].append([l_to_idx[arr], 1])
        # print(g)

        def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
            # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
            dist = [inf] * n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return dist

        sta = l_to_idx[tuple(nums1)]
        end = l_to_idx[tuple(nums2)]
        dist = dijkstra(g, sta, m)
        return dist[end]







so = Solution()
print(so.minSplitMerge(nums1 = [3,1,2], nums2 = [1,2,3]))
print(so.minSplitMerge(nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1]))




