

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10 ** 9 + 7
        ans = nums[:]
        n = len(nums)
        hp = [[x, i] for i, x in enumerate(nums)]
        heapify(hp)
        while k:
            x, idx = heappop(hp)
            x *= multiplier
            heappush(hp, [x, idx])
            ans[idx] = x
            k -= 1
        ans = [x % MOD for x in ans]
        return ans



so = Solution()
print(so.getFinalState())




