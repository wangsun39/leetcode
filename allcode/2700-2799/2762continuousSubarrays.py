
from leetcode.allcode.competition.mypackage import *

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        l = 0
        ans = 0
        cnt = SortedList()
        cnt.add(nums[0])
        r = 1
        while l < n:
            while r < n and (len(cnt) == 0 or (abs(nums[r] - cnt[0]) <= 2 and abs(nums[r] - cnt[-1]) <= 2)):
                cnt.add(nums[r])
                r += 1
            m = r - l
            ans += m
            cnt.remove(nums[l])
            l += 1
        return ans



so = Solution()
print(so.continuousSubarrays([1, 100]))
print(so.continuousSubarrays([31,30,31,32]))
print(so.continuousSubarrays([5,4,2,4]))
print(so.continuousSubarrays([1,2,3]))




