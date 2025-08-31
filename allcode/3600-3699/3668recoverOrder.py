

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        map = {x: i for i, x in enumerate(order)}
        friends.sort(key=lambda x:map[x])
        return friends


so = Solution()
print(so.recoverOrder(order = [3,1,2,5,4], friends = [1,3,4]))




