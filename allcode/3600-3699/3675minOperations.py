

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def minOperations(self, s: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        arr = [26 - c2i[x] for x in s if x != 'a']
        if len(arr) == 0:
            return 0
        return max(arr)



so = Solution()
print(so.minOperations())




