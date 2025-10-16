# 给你一个仅由数字（0 - 9）组成的字符串 num 。
#
# 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
#
# 注意：
#
# 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
# 数字可以重新排序。
#
#
# 示例 1：
#
# 输入：num = "444947137"
# 输出："7449447"
# 解释：
# 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
# 可以证明 "7449447" 是能够形成的最大回文整数。
# 示例 2：
#
# 输入：num = "00009"
# 输出："9"
# 解释：
# 可以证明 "9" 能够形成的最大回文整数。
# 注意返回的整数不应含前导零。
#
#
# 提示：
#
# 1 <= num.length <= 105
# num 由数字（0 - 9）组成


from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        s = []
        single = -1
        for x in counter:
            if counter[x] % 2 == 0:
                s.append([x, counter[x]])
            else:
                if counter[x] > 1:
                    s.append([x, counter[x] - 1])
                if int(x) > single:
                    single = int(x)
        s.sort(reverse=True)
        if len(s) and s[0][0] == '0':
            if single != -1:
                return str(single)
            else:
                return '0'
        ans = ''
        for e in s:
            ans += (e[0] * (e[1] // 2))
        ans1 = ans[::-1]
        if single != -1:
            ans += str(single)
        return ans + ans1




so = Solution()
print(so.largestPalindromic("0"))
print(so.largestPalindromic("00"))
print(so.largestPalindromic("000"))
print(so.largestPalindromic("9"))
print(so.largestPalindromic("09"))
print(so.largestPalindromic("00009"))
print(so.largestPalindromic("444947137"))




