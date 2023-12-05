
from leetcode.allcode.competition.mypackage import *

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        # print(words)
        n = len(words)
        for i in range(1, n):
            if words[i][0] != words[i - 1][-1]:
                return False
        return words[0][0] == words[-1][-1]


so = Solution()
print(so.isCircularSentence("leetcode exercises sound delightful"))
print(so.isCircularSentence("eetcode"))
print(so.isCircularSentence("Leetcode is cool"))




