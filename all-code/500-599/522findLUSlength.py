from typing import List
import functools

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
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


so = Solution()
print(so.findLUSlength(["aabbcc", "aabbcc","cb","abc"]))
print(so.findLUSlength(['abc', 'bdd', 'aaab', 'bbas']))
print(so.findLUSlength(['abcd', 'bdd']))

