from typing import List
import bisect
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codeList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabetaList = "abcdefghijklmnopqrstuvwxyz"
        a2cMap = dict(zip(alphabetaList, codeList))
        def a2c(word):
            res = ''
            for i in word:
                res += a2cMap[i]
            return res
        def c2n(code):
            time = 1
            res = 0
            for i in reversed(code):
                if i == '.':
                    res += time
                time *= 2
            return int(str(len(code)) + str(res))

        codeSet = set()
        for word in words:
            codeSet.add(c2n(a2c(word)))
        return len(codeSet)






so = Solution()
print(so.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


