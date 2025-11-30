

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            s = str(x)
            ss = s[::-1]
            return int(ss)
        ans = inf
        n = len(nums)
        # for i, x in enumerate(nums):
        #     y = reverse(x)
        #     if y in pos:
        #         ans = min(ans, i - pos[y])
        #     pos[x] = i
        pos = {}
        for i in range(n - 1, -1, -1):
            x = nums[i]
            y = reverse(x)
            if y in pos:
                ans = min(ans, pos[y] - i)
            pos[x] = i

        return ans if ans < inf else -1



so = Solution()
print(so.minMirrorPairDistance([120,21]))
print(so.minMirrorPairDistance([12,21,45,33,54]))




