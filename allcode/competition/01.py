

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s = sum(apple)
        ss = 0
        for i, x in enumerate(capacity):
            ss += x
            if ss >= s:
                return i + 1





so = Solution()
print(so.minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2]))
print(so.minimumBoxes(apple = [5,5,5], capacity = [2,4,2,7]))




