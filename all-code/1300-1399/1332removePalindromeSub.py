


from typing import List

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if s[:n // 2] == s[n - n // 2:][::-1]:
            return 1
        return 2


so = Solution()
print(so.removePalindromeSub("ababa"))
print(so.removePalindromeSub("abb"))
print(so.removePalindromeSub("baabb"))




