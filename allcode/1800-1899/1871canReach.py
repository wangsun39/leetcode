# 给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：
#
# i + minJump <= j <= min(i + maxJump, s.length - 1) 且
# s[j] == '0'.
# 如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "011010", minJump = 2, maxJump = 3
# 输出：true
# 解释：
# 第一步，从下标 0 移动到下标 3 。
# 第二步，从下标 3 移动到下标 5 。
# 示例 2：
#
# 输入：s = "01101110", minJump = 2, maxJump = 3
# 输出：false
#
#
# 提示：
#
# 2 <= s.length <= 105
# s[i] 要么是 '0' ，要么是 '1'
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1': return False

        q = deque([0])
        mx = 0  # BFS 搜索到的最大下标
        while q:
            x = q.popleft()
            lo, hi = max(mx, x + minJump), max(mx, x + maxJump)
            hi = min(hi, n - 1)
            mx = max(mx, hi)
            for y in range(lo, hi + 1):
                if y == n - 1:
                    return True
                if s[y] == '0':
                    q.append(y)
        return False

so = Solution()
print(so.canReach(s = "0100100010", minJump = 3, maxJump = 4))
print(so.canReach(s = "000000", minJump = 2, maxJump = 4))
print(so.canReach(s = "011010", minJump = 2, maxJump = 3))
print(so.canReach(s = "01101110", minJump = 2, maxJump = 3))




