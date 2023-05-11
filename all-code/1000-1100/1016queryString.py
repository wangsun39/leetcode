# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
#
# 子字符串 是字符串中连续的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "0110", n = 3
# 输出：true
# 示例 2：
#
# 输入：s = "0110", n = 4
# 输出：false
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 109


from typing import List
from functools import lru_cache

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        m = len(s)
        mx = m * (m + 1) // 2  # s 的所有子串个数
        if mx < n:
            return False
        vis = set()  # 出现的数字
        def check(i):  # 检查从第i个字符开始的子串
            cur = int(s[i])
            vis.add(cur)
            while i + 1 < m:
                cur = cur * 2 + int(s[i + 1])
                if cur > n:
                    return
                vis.add(cur)
                i += 1
            return
        for i in range(m):
            check(i)
        vis -= {0}
        return len(vis) == n



obj = Solution()
print(obj.queryString(s = "1", n = 1))
print(obj.queryString(s = "0110", n = 3))
print(obj.queryString(s = "0110", n = 4))

