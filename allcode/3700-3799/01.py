

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dd = defaultdict(list)
        for i, x in enumerate(nums):
            dd[x].append(i)
        ans = inf
        for arr in dd.values():
            if len(arr) < 3: continue
            for i in range(len(arr) - 2):
                ans = min(ans, (arr[i + 2] - arr[i]) * 2)
        return ans if ans < inf else -1



so = Solution()
print(so.minimumDistance(nums = [1,2,1,1,3]))




