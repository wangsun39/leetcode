# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
#
# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
# 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
# 返回k可能最大值。
#
#
#
# 示例 1：
#
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
# 示例 2：
#
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。
# 示例 3：
#
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
#
#
# 提示：
#
# 1 <= text.length <= 1000
# text 仅由小写英文字符组成

from typing import List, Optional
from collections import deque, defaultdict
from functools import cache



class Solution:
    def longestDecomposition1(self, text: str) -> int:

        @cache
        def dfs(i, j):  # 计算 text[i: j + 1] 子问题
            if i > j: return 0
            if i == j:
                return 1
            m = j - i + 1
            k = 1
            res = 1
            while k <= m // 2:
                if text[i: i + k] == text[j - k + 1 : j + 1]:
                    res = max(res, dfs(i + k, j - k) + 2)
                k += 1
            return res
        return dfs(0, len(text) - 1)

    def longestDecomposition(self, text: str) -> int:
        # 贪心的做法
        def dfs(i, j):  # 计算 text[i: j + 1] 子问题
            if i > j: return 0
            if i == j:
                return 1
            m = j - i + 1
            k = 1
            while k <= m // 2:
                if text[i: i + k] == text[j - k + 1 : j + 1]:
                    return dfs(i + k, j - k) + 2
                k += 1
            return 1
        return dfs(0, len(text) - 1)



obj = Solution()
print(obj.longestDecomposition("elvtoelvto"))
print(obj.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(obj.longestDecomposition("merchant"))
print(obj.longestDecomposition("antaprezatepzapreanta"))

