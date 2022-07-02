
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def getAnotherHalf():  # 找到对应右括号的相对位置
            rightPos = [-1] * len(S)
            stack = []
            for i, e in enumerate(S):
                if '(' == e:
                    stack.append(i)
                else:
                    left = stack.pop()
                    rightPos[left] = i - left
            return rightPos
        if '' == S:
            return 0
        rightPos = getAnotherHalf()
        print(rightPos)
        def scoreRecur(ss):
            if 2 == len(ss):
                return 1
            if len(ss) == ss[0] + 1:   # (....)
                return 2 * scoreRecur(ss[1:-1])
            if 1 == ss[0]:   # ()...
                return 1 + scoreRecur(ss[2:])
            # (...)...
            return 2 * scoreRecur(ss[1:ss[0]]) + scoreRecur(ss[ss[0] + 1:])
        return scoreRecur(rightPos)

    def scoreOfParentheses1(self, S):  # 官方解法
        stack = [0]  # The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)  # 内层括号对外层的影响：至少是1就是(), 其他情况就是 *2

        return stack.pop()


so = Solution()

print(so.scoreOfParentheses( "(())"))
print(so.scoreOfParentheses( "()()"))
print(so.scoreOfParentheses( "(()(()))"))


