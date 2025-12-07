

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def trans(x):
            s = str(bin(x)[2:])[::-1]
            return int(s, 2)
        nums.sort(key=lambda x:[trans(x), x])
        return nums



so = Solution()
print(so.sortByReflection(nums = [4,5,4]))




