# 给你两个字符串 s 和 part ，请你对 s 反复执行以下操作直到 所有 子字符串 part 都被删除：
#
# 找到 s 中 最左边 的子字符串 part ，并将它从 s 中删除。
# 请你返回从 s 中删除所有 part 子字符串以后得到的剩余字符串。
#
# 一个 子字符串 是一个字符串中连续的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "daabcbaabcbc", part = "abc"
# 输出："dab"
# 解释：以下操作按顺序执行：
# - s = "daabcbaabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。
# - s = "dabaabcbc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。
# - s = "dababc" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。
# 此时 s 中不再含有子字符串 "abc" 。
# 示例 2：
#
# 输入：s = "axxxxyyyyb", part = "xy"
# 输出："ab"
# 解释：以下操作按顺序执行：
# - s = "axxxxyyyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。
# - s = "axxxyyyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。
# - s = "axxyyb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。
# - s = "axyb" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。
# 此时 s 中不再含有子字符串 "xy" 。
#
#
# 提示：
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s 和 part 只包小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)

        pi = [0] * m  # 前缀子串 part[:i + 1] 的真前缀和真后缀的最长匹配
        c = 0
        for i in range(1, m):
            v = part[i]
            while c and part[c] != v:
                c = pi[c - 1]
            if part[c] == v:
                c += 1
            pi[i] = c

        stack = []
        for x in s:
            if len(stack) == 0:
                if x == part[0]:
                    stack.append([x, 1])
                else:
                    stack.append([x, 0])
            else:
                p = stack[-1][1]  # 已匹配长度
                while p and x != part[p]:
                    p = pi[p - 1]
                if x == part[p]:
                    stack.append([x, p + 1])
                else:
                    stack.append([x, 0])
            if stack[-1][1] == m:
                for _ in range(m):
                    stack.pop()

        ans = [x[0] for x in stack]
        return ''.join(ans)



so = Solution()
print(so.removeOccurrences(s = "daabcbaabcbc", part = "abc"))
print(so.removeOccurrences("kpygkivtlqoockpygkivtlqoocssnextkqzjpycbylkaondsskpygkpygkivtlqoocssnextkqzjpkpygkivtlqoocssnextkqzjpycbylkaondsycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi", "kpygkivtlqoocssnextkqzjpycbylkaonds"))


