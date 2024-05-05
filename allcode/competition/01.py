

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        for i in '@#$':
            if i in word:
                return False
        flg = 0
        for i in word:
            if i in 'aeiouAEIOU':
                flg |= 1
            elif i.isalpha() and i not in 'aeiouAEIOU':
                flg |= 2
        return flg == 3


so = Solution()
print(so.isValid("234Adas"))
print(so.isValid("b3"))
print(so.isValid("a3$e"))
print(so.isValid("234Adas"))




