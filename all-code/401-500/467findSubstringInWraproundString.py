from collections import defaultdict
class Solution:
    def findSubstringInWraproundString1(self, p):
        alphaDict = {}
        ''' 记录每个字母结尾的最长连续字串的长度，
        如：‘a': 10 表示a开头的顺序字串最大长度是10
        最终返回值就是 所有长度之和'''
        total_len = len(p)
        if total_len <= 1:
            return total_len
        last_c = p[0]
        consective_len = 1
        alphaDict[last_c] = 1
        for i in range(1, total_len):
            if ord(p[i]) - ord(last_c) == 1 or ('z' == last_c and 'a' == p[i]):
                consective_len += 1
            else:
                consective_len = 1
            if p[i] not in alphaDict or alphaDict[p[i]] < consective_len:
                alphaDict[p[i]] = consective_len
            last_c = p[i]
        sum = 0
        print(alphaDict)
        for key in alphaDict:
            sum += alphaDict[key]
        return sum

    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, e in enumerate(p):
            if i > 0 and (ord(e) - ord(p[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[e] = max(dp[e], k)
        return sum(dp.values())






so = Solution()
print(so.findSubstringInWraproundString('abcdfe'))
print(so.findSubstringInWraproundString('xyzabcdfe'))
#print(so.diffWaysToCompute("2*3-4*5"))

