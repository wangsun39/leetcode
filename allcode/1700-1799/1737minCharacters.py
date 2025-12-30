# 给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。
#
# 操作的最终目标是满足下列三个条件 之一 ：
#
# a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
# b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
# a 和 b 都 由 同一个 字母组成。
# 返回达成目标所需的 最少 操作数。
#
#
#
# 示例 1：
#
# 输入：a = "aba", b = "caa"
# 输出：2
# 解释：满足每个条件的最佳方案分别是：
# 1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
# 2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
# 3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
# 最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
# 示例 2：
#
# 输入：a = "dabadd", b = "cda"
# 输出：3
# 解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
#
#
# 提示：
#
# 1 <= a.length, b.length <= 105
# a 和 b 只由小写字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        a = [c2i[x] for x in a]
        b = [c2i[x] for x in b]
        mx_a, mn_a = max(a), min(a)
        mx_b, mn_b = max(b), min(b)
        n1, n2 = len(a), len(b)
        nums1 = [0] * 26
        nums2 = [0] * 26
        for x in a:
            nums1[x] += 1
        for x in b:
            nums2[x] += 1

        def calc1(a1, a2, mx1):  # 返回 a1 < a2
            res = inf
            if mx1 < 25:
                s1, s2, start = 0, sum(a2[:mx1 + 1]), mx1
            else:
                s1, s2, start = a1[mx1], sum(a2[: mx1]), mx1 - 1
            for hi_a1 in range(start, -1, -1):
                res = min(res, s1 + s2)
                s1 += a1[hi_a1]
                s2 -= a2[hi_a1]
            return res

        ans = min(calc1(nums1, nums2, mx_a), calc1(nums2, nums1, mx_b))
        for i in range(26):
            ans = min(ans, n1 - nums1[i] + n2 - nums2[i])
        return ans


so = Solution()
print(so.minCharacters(a = "zzp", b = "ymdtz"))
print(so.minCharacters(a = "d", b = "dcced"))
print(so.minCharacters(a = "d", b = "c"))
print(so.minCharacters(a = "aba", b = "caa"))


