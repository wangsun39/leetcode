from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        N = len(s)
        for i in range(N // 2):
            s[i], s[N-i-1] = s[N-i-1], s[i]
        return



so = Solution()
s = ["h","e","l","l","o"]
so.reverseString(s)
print(s)




