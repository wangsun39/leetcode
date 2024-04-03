

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        for bit in range(30, -1, -1):
            count = 0
            for i in range(n):
                if (nums[i] >> bit) & 1:
                    count += 1
            if count >= k:
                result |= (1 << bit)
                k -= 1
            if k == 0:
                break

        return result


so = Solution()
print(so.minOrAfterOperations(nums = [3,5,3,2,7], k = 2))




