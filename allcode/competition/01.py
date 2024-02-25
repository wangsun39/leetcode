

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(v <= 2 for v in counter.values())


so = Solution()
print(so.isPossibleToSplit([1,1,2,2,3,4]))
print(so.isPossibleToSplit([1,1,1,1]))




