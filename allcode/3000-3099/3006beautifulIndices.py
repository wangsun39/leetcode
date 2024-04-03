# 给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。
#
# 如果下标 i 满足以下条件，则认为它是一个 美丽下标：
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
# 1 <= k <= s.length <= 105
# 1 <= a.length, b.length <= 10
# s、a、和 b 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        idx_i = []
        idx_j = []
        n = len(s)
        for i in range(n):
            if s[i:].startswith(a):
                idx_i.append(i)
            if s[i:].startswith(b):
                idx_j.append(i)
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




