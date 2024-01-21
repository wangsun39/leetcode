

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        counter = sorted([[k, v] for k, v in counter.items()], key=lambda x:x[1], reverse=True)
        d = defaultdict(int)
        ans = 0
        idx = 0
        for k, v in counter:
            d[idx] += 1
            ans += v * d[idx]
            idx += 1
            idx %= 8
        return ans


so = Solution()
print(so.minimumPushes("abcde"))
print(so.minimumPushes("xyzxyzxyzxyz"))
print(so.minimumPushes("aabbccddeeffgghhiiiiii"))




