# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
#
# 示例 1：
#
# 输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
# 示例 2：
#
# 输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
# 示例 3：
#
# 输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
# 示例 4：
#
# 输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
# 提示：
#
# 1 <= len(pattern) <= 1000
# 0 <= len(value) <= 1000
# 你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        m, n = len(pattern), len(value)
        if n == 0: return m == 1
        pattern = list(pattern)
        if pattern[0] == 'b':
            pattern = ['b' if 'a' == pattern[i] else 'a' for i in range(m)]
        na = pattern.count('a')
        nb = m - na

        for la in range(n + 1):
            if n < na * la or (nb and (n - na * la) % nb != 0): continue
            if nb:
                lb = (n - na * la) // nb
            else:
                lb = 0
            if la == lb == 0: continue
            cur = 0
            matched = True
            a, b = '', ''
            for x in pattern:
                if x == 'a':
                    if a == '':
                        a = value[cur: cur + la]
                    else:
                        if a != value[cur: cur + la]:
                            matched = False
                            break
                    cur += la
                else:
                    if b == '':
                        if a == value[cur: cur + lb]: continue
                        b = value[cur: cur + lb]
                    else:
                        if b != value[cur: cur + lb]:
                            matched = False
                            break
                    cur += lb
            if matched and cur == n:
                return True
        return False



so = Solution()
print(so.patternMatching(pattern = "abbaa", value = "dogdogdogdogdog"))
print(so.patternMatching(pattern = "abb", value = "jwwwwjttwwwwjtt"))
print(so.patternMatching(pattern = "aaaa", value = "dogcatcatdog"))





