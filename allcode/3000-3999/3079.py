

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            s = str(x)
            l = list(s)
            mx = max(l)
            ans += int(''.join([mx] * len(l)))
        return ans



so = Solution()
print(so.sumOfEncryptedInt([1,2,3]))
print(so.sumOfEncryptedInt([10,21,31]))




