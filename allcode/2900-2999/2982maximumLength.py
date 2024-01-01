

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        start = 0
        d = defaultdict(list)  # 记录每个字符出现的连续子串长度
        for i, x in enumerate(s[1:], 1):
            ch = s[start]
            if x == ch:
                continue
            d[ch].append(i - start)
            start = i
        d[s[start]].append(n - start)
        ans = -1
        for ll in d.values():
            ll.sort(reverse=True)
            if ll[0] > 2:
                ans = max(ans, ll[0] - 2)
            if len(ll) >= 3:
                ans = max(ans, ll[2])
            if len(ll) >= 2 and ll[1] >= ll[0] - 1 > 0:
                ans = max(ans, ll[0] - 1)
        return ans




so = Solution()
print(so.maximumLength("jicja"))
print(so.maximumLength("aada"))
print(so.maximumLength("aaaa"))
print(so.maximumLength("abcdef"))
print(so.maximumLength("abcaba"))




