
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        if a == b:
            return -1
        else:
            return len(a)




so = Solution()
print(so.findLUSlength('abc', 'bdd'))

