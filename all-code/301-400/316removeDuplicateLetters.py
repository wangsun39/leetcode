from collections import defaultdict
class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        def findMinLetter(s):
            if 0 == len(s):
                return None, []
            minLetter, pos = s[0], [0]
            for idx, e in enumerate(s[1:]):
                if e < minLetter:
                    minLetter, pos = e, [idx+1]
                elif e == minLetter:
                    pos.append(idx+1)
            return minLetter, pos
        def findMaxLetter(s):
            if 0 == len(s):
                return None, []
            maxLetter, pos = s[0], [0]
            for idx, e in enumerate(s[1:]):
                if e > maxLetter:
                    maxLetter, pos = e, [idx+1]
                elif e == maxLetter:
                    pos.append(idx+1)
            return maxLetter, pos
        def removeDuplicateMax(s):
            maxLetter, pos = findMaxLetter(s)
            res = s
            for i in pos[-2::-1]:
                res = res[:i] + res[i+1:]
            return res
        def recurRemove(s):
            if len(s) < 2:
                return s
            if len(s) == 2:
                return s[0] if s[0] == s[1] else s
            s = removeDuplicateMax(s)
            minLetter, pos = findMinLetter(s)
            res = s
            for i in pos[:0:-1]:
                res = res[:i] + res[i+1:]
            if 0 == pos[0]:
                return minLetter + recurRemove(res[1:])
            if pos[0] == len(res)-1:
                return recurRemove(res[:-1]) + minLetter
            s1, s2 = recurRemove(res[:pos[0]]), recurRemove(res[pos[0]+1:])
            if s1 == s2:
                return minLetter + s2
            S1, S2 = set(s1), set(s2)
            if 0 == len(S1 & S2):
                return s1 + minLetter + s2
            S3, S4 = S1 & S2, S1 - S2  # 分别是：前后两个字符串相同的元素，前一个字符串有而后一个字符串没有的元素
            if 0 == len(S4):
                return minLetter + s2
            # s1中pos_maxS4位置之前的公共元素保留，删除对应s2中的那个相应元素，
            # s1中pos_maxS4位置之后的公共元素删除，保留对应s2中的那个相应元素
            res1, res2 = s1, s2
            for i in range(len(s1)-1, -1, -1):
                if s1[i] in S3:
                    if i+1 == len(s1) or s1[i] > s1[i+1]:
                        res1 = res1[:i] + res1[i+1:]
                    else:
                        res2 = res2.replace(s1[i], '')
            return res1 + minLetter + res2
        return recurRemove(s)
    def removeDuplicateLetters(self, s: str) -> str:
        maxIdxDict = {}
        for idx, e in enumerate(s):
            maxIdxDict[e] = idx
        stack = []
        for idx, e in enumerate(s):
            if e in stack:
                continue
            while len(stack) > 0 and stack[-1] > e and maxIdxDict[stack[-1]] > idx:
                stack.pop()
            stack.append(e)
        return ''.join(stack)


so = Solution()
print(so.removeDuplicateLetters("rzoraz"))
print(so.removeDuplicateLetters("ofeggkyuyjsrzornpdguwzizqszpi"))
print('bac' == so.removeDuplicateLetters("bbcaac"))
print('bac' == so.removeDuplicateLetters("cbac"))
print(so.removeDuplicateLetters('aa'))
print(so.removeDuplicateLetters('eabaazdera'))
print(so.removeDuplicateLetters('aeababzdera'))
print(so.removeDuplicateLetters('cbacdcbc'))
#print(so.diffWaysToCompute("2*3-4*5"))

