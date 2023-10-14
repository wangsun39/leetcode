
from leetcode.allcode.competition.mypackage import *


class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        s = set(expeditions[0].split('->'))
        def f(exp):
            if len(exp) == 0: return 0
            res = 0
            l = exp.split('->')
            for x in l:
                if x not in s:
                    res += 1
                    s.add(x)
            return res

        mx = 0
        ans = -1
        for i, x in enumerate(expeditions[1:], 1):
            cur = f(x)
            if mx < cur:
                mx = cur
                ans = i
        return ans



so = Solution()
print(so.adventureCamp(["Alice->Dex","","Dex"]))
print(so.adventureCamp(["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]))
print(so.adventureCamp(["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]))




