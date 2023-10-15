

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestBeautifulSubstring1(self, s: str, k: int) -> str:
        n = len(s)
        if k == 1:
            return '1' if '1' in s else ''
        cur = 1 if '1' in s else 0
        start = 0
        mil = inf
        miv = ''
        for i, x in enumerate(s[1:], 1):
            if x == '0':
                continue
            cur += 1
            if cur < k:
                continue
            if i - start < mil:
                mil = i - start
                miv = s[i + 1 - mil: i + 1]
            elif i - start == mil:
                if miv > s[i + 1 - mil: i + 1]:
                    miv = s[i + 1 - mil: i + 1]
            start += 1
            while start <= i and s[start] == '0':
                start += 1
            cur -= 1
        return miv

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        mil = inf
        miv = ''
        if k == 1:
            return '1' if '1' in s else ''
        for i in range(n):
            # if i == '0': continue
            cnt = 0
            for j in range(i, n):
                if s[j] == '1':
                    cnt += 1
                    if cnt == k:
                        if j - i + 1 < mil:
                            miv = s[i: j + 1]
                            mil = j - i + 1
                        elif j - i + 1 == mil:
                            miv = min(miv, s[i: j + 1])
                        break
        return miv



so = Solution()
print(so.shortestBeautifulSubstring("1100100101011001001", 7))
print(so.shortestBeautifulSubstring("11000111", 1))
print(so.shortestBeautifulSubstring(s = "100011001", k = 3))
print(so.shortestBeautifulSubstring(s = "1011", k = 2))
print(so.shortestBeautifulSubstring(s = "000", k = 1))




