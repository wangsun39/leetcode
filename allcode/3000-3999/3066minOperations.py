

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        cnt = 0
        while len(nums) >= 2:
            if nums[0] >= k:
                break
            x = heappop(nums)
            y = heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heappush(nums, z)
            cnt += 1
        return cnt


so = Solution()
print(so.minOperations(nums = [2,11,10,1,3], k = 10))
print(so.minOperations(nums = [1,1,2,4,9], k = 20))




