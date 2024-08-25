

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
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
        return ans




so = Solution()
print(so.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
print(so.getFinalState(nums = [1,2], k = 3, multiplier = 4))




