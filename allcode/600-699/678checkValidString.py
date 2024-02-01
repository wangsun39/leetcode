class Solution:
    def checkValidString(self, s: str) -> bool:
        def matchBracket(s):
            res = ''
            for e in s:
                if e in ('(', '*'):
                    res += e
                else:
                    pos = res.rfind('(')
                    if -1 == pos:
                        res += e
                    else:
                        res = res[:pos] + res[pos+1:]
            return res

        s1 = matchBracket(s)
        leftBracket, rightBracket, star = 0, 0, 0
        for i in s1:
            if '(' == i:
                star = min(star, leftBracket)
                leftBracket += 1
            elif ')' == i:
                if leftBracket > 0:
                    leftBracket -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
            else:
                star += 1

        return 0 == leftBracket or leftBracket <= star

    def checkValidString1(self, s: str) -> bool:  # 简化一点的形式
        leftBracket, star, = 0, 0
        for e in s:
            if '(' == e:
                star = min(star, leftBracket)
                leftBracket += 1
            elif ')' == e:
                if leftBracket > 0:
                    leftBracket -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
            else:
                star += 1
        return leftBracket <= star



obj = Solution()
print(obj.checkValidString("(*()"))
print(obj.checkValidString("(**((*"))
print(obj.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
print(obj.checkValidString("()"))
print(obj.checkValidString("(*)"))
print(obj.checkValidString("(*))"))
