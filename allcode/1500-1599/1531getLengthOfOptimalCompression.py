# 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。
#
# 注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。
#
# 给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。
#
# 请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。
#
#
#
# 示例 1：
#
# 输入：s = "aaabcccd", k = 2
# 输出：4
# 解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
# 示例 2：
#
# 输入：s = "aabbaa", k = 2
# 输出：2
# 解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
# 示例 3：
#
# 输入：s = "aaaaaaaaaaa", k = 0
# 输出：3
# 解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
#
#
# 提示：
#
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s 仅包含小写英文字母

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        c1 = []  # 记录各段长度
        i = 1
        n = len(s)
        acc = 1
        while i <= n:
            if i == n or s[i] != s[i - 1]:
                c1.append(acc)
                acc = 1
            else:
                acc += 1
            i += 1
        ans = 0  # 压缩后长度
        c2 = []  # 记录当前段的长度需要减少多少才能使字符标识的长度减1
        def getLen(l):
            if l == 1:
                return 1
            if x < 10:
                return x - 1
            if x < 100:
                return x - 9
            return x - 99
        for x in c1:
            if x == 1:
                c2.append(1)
                ans += 1
            elif x < 10:
                c2.append(x - 1)
                ans += 2
            elif x < 100:
                c2.append(x - 9)
                ans += 3
            else:
                c2.append(x - 99)
                ans += 4
        hp = []
        for i, x in enumerate(c2):
            heappush(hp, [x, i])

        while k > 0 and len(hp):
            cnt, idx = heappop(hp)
            if cnt > k:
                return ans
            k -= cnt
            ans -= 1
            c1[idx] -= cnt
            if c1[idx] == 0: # 这个子段已被删除
                continue
            # x2 = getLen(c1[idx])  # 需要删掉x2个字符，子段长度能减1
            heappush(hp, [getLen(c1[idx]), idx])
        return ans





so = Solution()
print(so.getLengthOfOptimalCompression(s = "aabbaa", k = 2))
print(so.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
print(so.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))




