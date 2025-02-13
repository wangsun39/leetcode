from typing import List
from collections import defaultdict

import time
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def getParenthesesFlag(orig_len):  # 为每个括号标记是否能删除的标记,并计算出最终的长度
            Flag = [True] * len(s)
            leftList, leftValid = [], 0
            finial_len = orig_len
            for i, e in enumerate(s):
                if '(' == e:
                    leftValid += 1
                    leftList.append(i)
                elif ')' == e:
                    leftValid -= 1
                    if leftValid <= 0:
                        for j in leftList:
                            Flag[j] = False
                        leftList = []
                        if leftValid < 0:
                            leftValid = 0
                            finial_len -= 1
                else:
                    Flag[i] = False
            rightList, rightValid = [], 0
            for i in range(len(s)-1, -1, -1):
                if ')' == s[i]:
                    rightValid += 1
                    rightList.append(i)
                elif '(' == s[i]:
                    rightValid -= 1
                    if rightValid <= 0:
                        for j in rightList:
                            Flag[j] = False
                        rightList = []
                        if rightValid < 0:
                            rightValid = 0
                            finial_len -= 1
                else:
                    Flag[i] = False
            return Flag, finial_len

        t1 = time.time()
        Flag, finial_len = getParenthesesFlag(len(s))
        seq = [[s[i], Flag[i]] for i in range(len(s))]
        print(seq)
        print(finial_len)
        t2 = time.time()
        print(t2-t1)

        def isValid(ss):
            nonlocal count
            count += 1
            left, right = 0, 0
            for e in ss:
                if '(' == e[0]:
                    left += 1
                elif ')' == e[0]:
                    right += 1
                    if right > left:
                        return False
            return left == right

        res = set()
        count = 0
        def bfs(ss, start):
            if len(ss) < finial_len:
                return
            str = ''
            for i in ss:
                str += i[0]
            if isValid(ss):
                res.add(str)
                return
            calc = set()
            for i in range(start, len(ss)):
                if not ss[i][1]:
                    continue
                if str[:i] + str[i+1:] in calc: # 过滤重复的计算
                    continue
                calc.add(str[:i] + str[i+1:])
                sss = ss[:i] + ss[i+1:]
                bfs(sss, i)

        t1 = time.time()
        bfs(seq, 0)
        t2 = time.time()
        print(count, t2-t1)
        return list(res)



    def removeInvalidParentheses1(self, s: str) -> List[str]:
        count = 0
        def isvalid(string):  # 判断括号串是否合法
            nonlocal count
            count += 1
            l_minus_r = 0
            for c in string:
                if c == '(':
                    l_minus_r += 1
                elif c == ')':
                    l_minus_r -= 1
                    if l_minus_r < 0:
                        return False
            return l_minus_r == 0

        level = {s}

        while True:  # BFS
            valid = list(filter(isvalid, level))
            if valid:
                print(count)
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}

so = Solution()
print(so.removeInvalidParentheses("()())())))())(()"))
print(so.removeInvalidParentheses1("()())())))())(()"))
# print(so.removeInvalidParentheses("())(((()m)("))
# print(so.removeInvalidParentheses("()()()"))
# print(so.removeInvalidParentheses("()())()"))
# print(so.removeInvalidParentheses1("()())()"))
# print(so.removeInvalidParentheses("(a)())()"))
# print(so.removeInvalidParentheses(")("))

