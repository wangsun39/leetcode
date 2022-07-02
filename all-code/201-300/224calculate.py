class Solution:
    def calculate(self, s: str) -> int:
        stack = [[1, 0]]
        sign = 1
        i = 0
        while i < len(s):
            if '(' == s[i]:
                stack.append([sign, 0])
                sign = 1
            elif ')' == s[i]:
                e = stack.pop()
                stack[-1][1] += (e[0] * e[1])
            elif s[i].isdigit():
                cur = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    cur = cur * 10 + int(s[i+1])
                    i += 1
                stack[-1][1] += (sign * cur)
            elif '+' == s[i]:
                sign = 1
            elif '-' == s[i]:
                sign = -1
            i += 1
        return stack[0][1]



so = Solution()
print(so.calculate("1 + 1"))
print(so.calculate(" 2-1 + 2 "))
print(so.calculate( "(1+(4+5+2)-3)+(6+8)"))

