
import functools
from leetcode.allcode.competition.mypackage import *

class Solution:
    def findLUSlength1(self, strs: List[str]) -> int:
        def cmp(x, y): # return 1 if x <y  -1 if x > y
            if len(x) != len(y):
                return 1 if len(x) < len(y) else -1
            return 1 if x > y else -1
        def isSub(a, b):
            # if len(a) >= len(b):
            #     return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                    if i == len(a):
                        return True
                else:
                    j += 1
            return False

        strs = sorted(strs, key=functools.cmp_to_key(cmp))
        print(strs)
        for i in range(len(strs)):
            next = False
            for j in range(i):
                if isSub(strs[i], strs[j]):
                    next = True
                    break
            if next:
                continue
            if i == len(strs) - 1 or strs[i] != strs[i + 1]:
                return len(strs[i])
        return -1

    def findLUSlength(self, strs: List[str]) -> int:
        counter = Counter(strs)
        counter = list(counter.items())
        counter.sort(key=lambda x:len(x[0]), reverse=True)
        def subs(a, b): # a是否是b的子序列
            bi = 0
            for ai, x in enumerate(a):
                while bi < len(b) and x != b[bi]:
                    bi += 1
                if bi == len(b):
                    return False
                bi += 1
            return True
        for i, [k, v] in enumerate(counter):
            if v > 1: continue
            found = True
            for j in range(i):
                if subs(k, counter[j][0]):
                    found = False
                    break
            if found:
                return len(k)
        return -1

so = Solution()
print(so.findLUSlength(["abcabc","abcabc","abcabc","abc","abc","cca"]))
print(so.findLUSlength(["aabbcc", "aabbcc","c","e","aabbcd"]))
print(so.findLUSlength(["aabbcc", "aabbcc","cb","abc"]))
print(so.findLUSlength(['abc', 'bdd', 'aaab', 'bbas']))
print(so.findLUSlength(['abcd', 'bdd']))

