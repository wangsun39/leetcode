

from leetcode.allcode.competition.mypackage import *

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        sl = SortedList()
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            x, f = nums[i], freq[i]
            if x in counter:
                sl.remove(counter[x])
            counter[x] += f
            sl.add(counter[x])
            ans[i] = sl[-1]
        return ans



so = Solution()
print(so.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]))
print(so.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]))




