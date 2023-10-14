
from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            sl = SortedList()
            sl.add(nums[i])
            cnt = 0
            for j in range(i + 1, n):
                pos = sl.bisect_left(nums[j])
                if pos == len(sl):
                    if nums[j] - sl[-1] > 1:
                        cnt += 1
                elif pos == 0:
                    if sl[0] - nums[j] > 1:
                        cnt += 1
                else:
                    if sl[pos] - sl[pos - 1] <= 1:
                        pass
                    else:
                        cnt -= 1
                        if nums[j] - sl[pos - 1] > 1:
                            cnt += 1
                        if sl[pos] - nums[j] > 1:
                            cnt += 1
                ans += cnt
                sl.add(nums[j])
        return ans

so = Solution()
print(so.sumImbalanceNumbers([3,1,2]))
print(so.sumImbalanceNumbers([1,3,3,3,5]))
print(so.sumImbalanceNumbers([1,3,2]))
print(so.sumImbalanceNumbers([2,3,1,4]))




