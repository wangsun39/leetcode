

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def minClose(x):
            s = str(x)
            if s == s[::-1]:
                return [x]
            n = len(s)
            m = n // 2
            if n & 1:
                h1 = int(s[:m + 1])
                h2 = h1 - 1
                h3 = h1 + 1
                v1 = int(str(h1) + str(h1)[:-1][::-1])
                if len(str(h2)) < len(str(h1)):
                    v2 = int(str(h2) + str(h2)[::-1])
                else:
                    v2 = int(str(h2) + str(h2)[:-1][::-1])
                if len(str(h3)) > len(str(h1)):
                    v3 = int(str(h3) + str(h3)[:-2][::-1])
                else:
                    v3 = int(str(h3) + str(h3)[:-1][::-1])
                return [v1, v2, v3]
            else:
                h1 = int(s[:m])
                h2 = h1 - 1
                h3 = h1 + 1
                v1 = int(s[:m] + s[:m][::-1])
                if h2 == 0:
                    v2 = 9
                else:
                    if len(str(h2)) < len(str(h1)):
                        v2 = int(str(h2) + '9' + str(h2)[::-1])
                    else:
                        v2 = int(str(h2) + str(h2)[::-1])
                if len(str(h3)) > len(str(h1)):
                    v3 = int(str(h3) + str(h3[:-1])[::-1])
                else:
                    v3 = int(str(h3) + str(h3)[::-1])
                return [v1, v2, v3]
        nums.sort()
        n = len(nums)
        if n & 1:
            v = minClose(nums[n // 2])
        else:
            n1, n2 = nums[n // 2], nums[n // 2 - 1]
            v1 = minClose(n1)
            v2 = minClose(n2)
            v = v1 + v2
        ans = inf
        for x in v:
            ans = min(ans, sum(abs(xx - x) for xx in nums))
        return ans


so = Solution()
print(so.minimumCost([101,104,107,126,130]))
print(so.minimumCost([1,2,3,4,5]))
print(so.minimumCost([10,12,13,14,15]))
print(so.minimumCost([22,33,22,33,22]))




