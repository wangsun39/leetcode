# 给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。
#
# 如果下标 i 满足以下条件，则认为它是一个 美丽下标 ：
#
# 0 <= i <= s.length - a.length
# s[i..(i + a.length - 1)] == a
# 存在下标 j 使得：
# 0 <= j <= s.length - b.length
# s[j..(j + b.length - 1)] == b
# |j - i| <= k
# 以数组形式按 从小到大排序 返回美丽下标。
#
#
#
# 示例 1：
#
# 输入：s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
# 输出：[16,33]
# 解释：存在 2 个美丽下标：[16,33]。
# - 下标 16 是美丽下标，因为 s[16..17] == "my" ，且存在下标 4 ，满足 s[4..11] == "squirrel" 且 |16 - 4| <= 15 。
# - 下标 33 是美丽下标，因为 s[33..34] == "my" ，且存在下标 18 ，满足 s[18..25] == "squirrel" 且 |33 - 18| <= 15 。
# 因此返回 [16,33] 作为结果。
# 示例 2：
#
# 输入：s = "abcd", a = "a", b = "a", k = 4
# 输出：[0]
# 解释：存在 1 个美丽下标：[0]。
# - 下标 0 是美丽下标，因为 s[0..0] == "a" ，且存在下标 0 ，满足 s[0..0] == "a" 且 |0 - 0| <= 4 。
# 因此返回 [0] 作为结果。
#
#
# 提示：
#
# 1 <= k <= s.length <= 5 * 105
# 1 <= a.length, b.length <= 5 * 105
# s、a、和 b 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        def build_prefix_table(pattern):
            length = len(pattern)
            lps = [0] * length  # 初始化前缀表

            i = 1
            length_of_longest_prefix = 0
            while i < length:
                if pattern[i] == pattern[length_of_longest_prefix]:
                    length_of_longest_prefix += 1
                    lps[i] = length_of_longest_prefix
                    i += 1
                else:
                    if length_of_longest_prefix != 0:
                        length_of_longest_prefix = lps[length_of_longest_prefix - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        def kmp_search(text, pattern):
            n = len(text)
            m = len(pattern)
            indices = []  # 用于存储匹配成功的起始下标


            lps = build_prefix_table(pattern)

            i, j = 0, 0
            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                    if j == m:
                        indices.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices
        idx_i = kmp_search(s, a)
        idx_j = kmp_search(s, b)

        ans = []
        for i in idx_i:
            p1 = bisect_left(idx_j, i - k)
            p2 = bisect_right(idx_j, i + k)
            if p2 - p1 > 0:
                ans.append(i)
        return ans


so = Solution()
print(so.beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15))
print(so.beautifulIndices(s = "abcd", a = "a", b = "a", k = 4))




