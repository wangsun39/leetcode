# 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。
#
# 返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。
#
#
#
# 示例 1:
#
# 输入: s = "aab"
# 输出: "aba"
# 示例 2:
#
# 输入: s = "aaab"
# 输出: ""
#
#
# 提示:
#
# 1 <= s.length <= 500
# s 只包含小写字母

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        counter = Counter(s)
        counter = sorted([[k, v] for k, v in counter.items()], key=lambda x: x[1], reverse=True)
        if len(counter) == 1 or counter[0][1] > (n + 1) // 2: return ''
        ans = [''] * n
        i = 0
        for k, v in counter:
            for _ in range(v):
                ans[i] = k
                i += 2
                if i > n - 1:
                    i = 1
        return ''.join(ans)


so = Solution()
print(so.reorganizeString(s = "aab"))




