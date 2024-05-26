

from leetcode.allcode.competition.mypackage import *

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        prei = 0
        ans = []
        for i in range(1, n):
            x = word[i]
            if x == word[prei]:
                if i - prei == 9:
                    ans.append('9' + x)
                    prei = i
            else:
                ans.append(str(i - prei) + word[i - 1])
                prei = i
        ans.append(str(n - prei) + word[-1])
        return ''.join(ans)


so = Solution()
print(so.compressedString(word = "abcde"))
print(so.compressedString(word = "aaaaaaaaaaaaaabb"))




