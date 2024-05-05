

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        ans = 0
        for w in words:
            ct = Counter(w)
            flg = True  # 是否掌握
            for k, v in ct.items():
                if v > counter[k]:
                    flg = False
                    break
            if flg:
                ans += len(w)
        return ans


so = Solution()
print(so.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(so.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))




