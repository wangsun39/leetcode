# 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
#
# 删除子字符串 "ab" 并得到 x 分。
# 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
# 删除子字符串"ba" 并得到 y 分。
# 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
# 请返回对 s 字符串执行上面操作若干次能得到的最大得分。
#
#
#
# 示例 1：
#
# 输入：s = "cdbcbbaaabab", x = 4, y = 5
# 输出：19
# 解释：
# - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
# - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
# - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
# - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
# 总得分为 5 + 4 + 5 + 5 = 19 。
# 示例 2：
#
# 输入：s = "aabbaaxybbaabb", x = 5, y = 4
# 输出：20
#
#
# 提示：
#
# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s 只包含小写英文字母。


# Definition for a binary tree node.
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        if x < y:
            ss = list(s)
            for i in range(n):
                if ss[i] == 'a': ss[i] = 'b'
                elif ss[i] == 'b': ss[i] = 'a'
            s = ''.join(ss)
            x, y = y, x
        ca = cb = ans = 0
        for i, u in enumerate(s):
            if u not in 'ab':
                ans += min(ca, cb) * y
                ca = cb = 0
            elif u == 'b':
                if ca:
                    ans += x
                    ca -= 1
                else:
                    cb += 1
            else:
                ca += 1
        ans += min(ca, cb) * y
        return ans


so = Solution()
print(so.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))




