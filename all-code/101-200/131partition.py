from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = {}
        def isPalindrome(s):
            i, N = 0, len(s)
            while i < N // 2:
                if s[i] != s[N-1-i]:
                    return False
                i += 1
            return True
        def helper(s):
            nonlocal d
            res = []
            i, N = 0, len(s)
            if 1 == N:
                return [[s[0]]]
            while i < N:
                if isPalindrome(s[:i+1]):
                    if s[i+1:] in d:
                        subStrSet = d[s[i+1:]]
                    else:
                        subStrSet = helper(s[i+1:])
                        d[s[i+1:]] = subStrSet
                    if i+1 == N:
                        res.append([s[:i+1]])
                    else:
                        for x in subStrSet:
                            res.append([s[:i+1]] + x)
                i += 1
            return res
        return helper(s)


so = Solution()
print(so.partition('aa'))
print(so.partition('aab'))


