

from leetcode.allcode.competition.mypackage import *

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        snums = deque(sorted([x, i] for i, x in enumerate(nums)))
        vis = set()
        s = sum(nums)
        ans = [0] * len(queries)
        for ii, [idx, k] in enumerate(queries):
            if idx not in vis:
                s -= nums[idx]
                vis.add(idx)
            j = k
            while j > 0 and len(snums):
                x, i = snums.popleft()
                if i not in vis:
                    j -= 1
                    vis.add(i)
                    s -= x
            ans[ii] = s
            if s == 0:
                break
        return ans


so = Solution()
print(so.unmarkedSumArray(nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]))
print(so.unmarkedSumArray(nums = [1,4,2,3], queries = [[0,1]]))




