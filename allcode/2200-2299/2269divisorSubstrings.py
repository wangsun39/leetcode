# 一个整数 num的k美丽值定义为num中符合以下条件的子字符串数目：
#
# 子字符串长度为k。
# 子字符串能整除 num 。
# 给你整数num 和k，请你返回num的 k 美丽值。
#
# 注意：
#
# 允许有前缀0。
# 0不能整除任何值。
# 一个 子字符串是一个字符串里的连续一段字符序列。
#
#
#
# 示例 1：
#
# 输入：num = 240, k = 2
# 输出：2
# 解释：以下是 num 里长度为 k 的子字符串：
# - "240" 中的 "24" ：24 能整除 240 。
# - "240" 中的 "40" ：40 能整除 240 。
# 所以，k 美丽值为 2 。
# 示例 2：
#
# 输入：num = 430043, k = 2
# 输出：2
# 解释：以下是 num 里长度为 k 的子字符串：
# - "430043" 中的 "43" ：43 能整除 430043 。
# - "430043" 中的 "30" ：30 不能整除 430043 。
# - "430043" 中的 "00" ：0 不能整除 430043 。
# - "430043" 中的 "04" ：4 不能整除 430043 。
# - "430043" 中的 "43" ：43 能整除 430043 。
# 所以，k 美丽值为 2 。
#
#
# 提示：
#
# 1 <= num <= 109
# 1 <= k <= num.length（将num视为字符串）


from leetcode.allcode.competition.mypackage import *
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        N = len(n)
        ans = 0
        for i in range(N - k + 1):
            s = int(n[i: i + k])
            if s != 0 and num % s == 0:
                ans += 1
        return ans



so = Solution()
print(so.divisorSubstrings(240, k = 2))
print(so.divisorSubstrings(430043, k = 2))




