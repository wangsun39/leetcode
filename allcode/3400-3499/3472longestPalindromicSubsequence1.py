# 给你一个字符串 s 和一个整数 k。
#
# 在一次操作中，你可以将任意位置的字符替换为字母表中相邻的字符（字母表是循环的，因此 'z' 的下一个字母是 'a'）。例如，将 'a' 替换为下一个字母结果是 'b'，将 'a' 替换为上一个字母结果是 'z'；同样，将 'z' 替换为下一个字母结果是 'a'，替换为上一个字母结果是 'y'。
#
# 返回在进行 最多 k 次操作后，s 的 最长回文子序列 的长度。
#
# 子序列 是一个 非空 字符串，可以通过删除原字符串中的某些字符（或不删除任何字符）并保持剩余字符的相对顺序得到。
#
# 回文 是正着读和反着读都相同的字符串。
#
#
#
# 示例 1：
#
# 输入: s = "abced", k = 2
#
# 输出: 3
#
# 解释:
#
# 将 s[1] 替换为下一个字母，得到 "acced"。
# 将 s[4] 替换为上一个字母，得到 "accec"。
# 子序列 "ccc" 形成一个长度为 3 的回文，这是最长的回文子序列。
#
# 示例 2：
#
# 输入: s = "aaazzz", k = 4
#
# 输出: 6
#
# 解释:
#
# 将 s[0] 替换为上一个字母，得到 "zaazzz"。
# 将 s[4] 替换为下一个字母，得到 "zaazaz"。
# 将 s[3] 替换为下一个字母，得到 "zaaaaz"。
# 整个字符串形成一个长度为 6 的回文。
#
#
#
# 提示:
#
# 1 <= s.length <= 200
# 1 <= k <= 200
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestPalindromicSubsequence1(self, s: str, k: int) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = [c2i[x] for x in s]
        n = len(s)
        ans = 1
        def dis(x, y):
            if x > y: x, y = y, x
            return min(y - x, x + 26 - y)
        def check1(mid):
            cnt = k
            for i in range(1, n):
                if mid - i < 0 or mid + i >= n:
                    return (i - 1) * 2 + 1
                d = dis(s[mid - i], s[mid + i])
                if d <= cnt:
                    cnt -= d
                else:
                    return (i - 1) * 2 + 1
            return 1
        def check2(mid):
            cnt = k
            if mid + 1 >= n: return 0
            for i in range(n):
                if mid - i < 0 or mid + 1 + i >= n:
                    return i * 2
                d = dis(s[mid - i], s[mid + 1 + i])
                if d <= cnt:
                    cnt -= d
                else:
                    return i * 2

        for i in range(n):
            ans = max(ans, check1(i), check2(i))

        return ans


    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = [c2i[x] for x in s]
        n = len(s)
        ans = 1
        def dis(x, y):
            if x > y: x, y = y, x
            return min(y - x, x + 26 - y)

        @cache
        def dfs(i, j, t):
            if i == j: return 1
            if i == j - 1:
                if dis(s[i], s[j]) <= t:
                    return 2
                return 1
            d = dis(s[i], s[j])
            if d > t:
                return max(dfs(i + 1, j, t), dfs(i, j - 1, t))
            return max(dfs(i + 1, j, t), dfs(i, j - 1, t), dfs(i + 1, j - 1, t - d) + 2)

        return dfs(0, n - 1, k)


so = Solution()
print(so.longestPalindromicSubsequence(s = "wehzr", k = 3))
print(so.longestPalindromicSubsequence(s = "alr", k = 5))
print(so.longestPalindromicSubsequence(s = "a", k = 20))
print(so.longestPalindromicSubsequence(s = "aaazzz", k = 4))
print(so.longestPalindromicSubsequence(s = "abced", k = 2))




