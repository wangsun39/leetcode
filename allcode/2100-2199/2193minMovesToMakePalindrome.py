# 给你一个只包含小写英文字母的字符串 s 。
#
# 每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。
#
# 请你返回将 s 变成回文串的 最少操作次数 。
#
# 注意 ，输入数据会确保 s 一定能变成一个回文串。
#
#
#
# 示例 1：
#
# 输入：s = "aabb"
# 输出：2
# 解释：
# 我们可以将 s 变成 2 个回文串，"abba" 和 "baab" 。
# - 我们可以通过 2 次操作得到 "abba" ："aabb" -> "abab" -> "abba" 。
# - 我们可以通过 2 次操作得到 "baab" ："aabb" -> "abab" -> "baab" 。
# 因此，得到回文串的最少总操作次数为 2 。
# 示例 2：
#
# 输入：s = "letelt"
# 输出：2
# 解释：
# 通过 2 次操作从 s 能得到回文串 "lettel" 。
# 其中一种方法是："letelt" -> "letetl" -> "lettel" 。
# 其他回文串比方说 "tleelt" 也可以通过 2 次操作得到。
# 可以证明少于 2 次操作，无法得到回文串。
#
#
# 提示：
#
# 1 <= s.length <= 2000
# s 只包含小写英文字母。
# s 可以通过有限次操作得到一个回文串。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # 贪心思路的简单证明
        # https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/solutions/1313466/tan-xin-zheng-ming-geng-da-shu-ju-fan-we-h57i/
        n = len(s)
        s = list(s)
        counter = Counter(s)
        ans = 0
        if n & 1:
            odds = [x for x, v in counter.items() if v & 1][0]
            podds = [i for i, x in enumerate(s) if x == odds]
            pmid = podds[len(podds) // 2]
            s[pmid] = '#'  # 中间点

        flg = False
        for i, x in enumerate(s):
            if i == n // 2: break
            if x == '#':  # 遇到中间点先不移动，直接跳过
                flg = True
                ans += (n // 2 - i)  # 中间点在后面的处理中不会在移动了，直到最后单独处理中间点，需要 n // 2 - i 步
                continue

            if flg:  # 遇到中间点之后，因为中间点没有动，实际i的最终位置是在i-1处
                i -= 1
            j = n - 1 - i
            if s[j] == x: continue
            t, s[j] = s[j], x
            ans += 1
            while s[j - 1] != x:
                t, s[j - 1] = s[j - 1], t
                j -= 1
                ans += 1
            s[j - 1] = t
        return ans

so = Solution()

print(so.minMovesToMakePalindrome("skwhhsk"))  # 2
print(so.minMovesToMakePalindrome("scpcyxprxxsjyjrww"))  # 42
print(so.minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii"))  # 163
print(so.minMovesToMakePalindrome("aabb"))
print(so.minMovesToMakePalindrome("letelt"))




