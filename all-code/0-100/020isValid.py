# 两数之和
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e in '([{':
                stack.append(e)
            else:
                if 0 == len(stack):
                    return False
                x = stack.pop()
                if '(' == x and ')' != e or '[' == x and ']' != e or '{' == x and '}' != e:
                    return False
        return 0 == len(stack)



so = Solution()
print(so.isValid("([)]"))
print(so.isValid("{[]}"))
