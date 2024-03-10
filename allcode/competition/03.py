

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        counter = Counter()
        sl = []
        for s in arr:
            ss = set()
            m = len(s)
            for i in range(m):
                for j in range(i, m):
                    ss.add(s[i: j + 1])
            sl.append(ss)
            for sub in ss:
                counter[sub] += 1
        n = len(arr)
        ans = [''] * n
        for i, x in enumerate(arr):
            for y in sl[i]:
                if counter[y] == 1 and (ans[i] == '' or len(ans[i]) > len(y) or (len(ans[i]) == len(y) and ans[i] > y)):
                    ans[i] = y
        return ans


so = Solution()
print(so.shortestSubstrings(arr = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]))
print(so.shortestSubstrings(arr = ["cab","ad","bad","c"]))
print(so.shortestSubstrings(arr = ["abc","bcd","abcd"]))




