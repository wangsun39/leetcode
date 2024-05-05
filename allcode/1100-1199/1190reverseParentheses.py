from typing import List
class Solution:
    def reverseParentheses(self, s: str) -> str:
        def findCloseParenthesis(s1):
            count = 0
            for k, v in enumerate(s1):
                if '(' == v:
                    count += 1
                elif ')' == v:
                    count -= 1
                    if 0 == count:
                        return k
        def recursive(s1):
            # print(111, s1)
            begin = s1.find('(')
            if -1 == begin:
                # print(222, s1)
                return s1
            end = findCloseParenthesis(s1[begin:]) + begin
            # print(333, s1[:begin] + ''.join(reversed(recursive(s1[begin+1:end]))) + s1[end+1:])
            return s1[:begin] + ''.join(reversed(recursive(s1[begin+1:end]))) + recursive(s1[end+1:])
        return recursive(s)



obj = Solution()
print(obj.reverseParentheses("ta()usw((((a))))"))
print(obj.reverseParentheses("(ed(et(oc))el)"))
#print(obj.reverseParentheses("(ed(et(oc))el)"))

