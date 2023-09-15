# 给你一个二进制字符串 s 和一个整数 k 。如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 true ，否则请返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "00110110", k = 2
# 输出：true
# 解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
# 示例 2：
#
# 输入：s = "0110", k = 1
# 输出：true
# 解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
# 示例 3：
#
# 输入：s = "0110", k = 2
# 输出：false
# 解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
#
#
# 提示：
#
# 1 <= s.length <= 5 * 105
# s[i] 不是'0' 就是 '1'
# 1 <= k <= 20


from typing import List
import math

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        vis = set()
        for i in range(n - k + 1):
            vis.add(int(s[i: i + k], 2))
            if len(vis) == 2 ** k:
                return True
        return False



so = Solution()
print(so.hasAllCodes("00110", 2))
print(so.hasAllCodes(s = "00110110", k = 2))
print(so.hasAllCodes(s = "0110", k = 1))
print(so.hasAllCodes(s = "0110", k = 2))




