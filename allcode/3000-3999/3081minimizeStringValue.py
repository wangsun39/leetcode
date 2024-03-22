

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counter = Counter(s)
        for k in ascii_lowercase: counter[k] = counter[k]
        cc = [[v, k] for k, v in counter.items() if k != '?']
        heapify(cc)
        num = counter['?']
        add = []
        l = list(s)
        cur = 0
        for _ in range(num):
            while l[cur] != '?':
                cur += 1
            v, k = heappop(cc)
            add.append(k)
            heappush(cc, [v + 1, k])
            cur += 1
        add.sort()
        for i, x in enumerate(l):
            if x == '?':
                l[i] = add.pop(0)
        return ''.join(l)


so = Solution()
print(so.minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
print(so.minimizeStringValue("a?a?"))
print(so.minimizeStringValue("???"))




