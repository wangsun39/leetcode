class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        res = 0
        for e in S:
            if '(' == e:
                left += 1
            elif ')' == e:
                if left > 0:
                    left -= 1
                else:
                    res += 1
        return res + left

so = Solution()
print(so.minAddToMakeValid("())"))
print(so.minAddToMakeValid("()"))
print(so.minAddToMakeValid("()))(("))
