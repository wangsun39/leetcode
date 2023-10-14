# 给你一个正整数 n ，你可以执行下述操作 任意 次：
#
# n 加上或减去 2 的某个 幂
# 返回使 n 等于 0 需要执行的 最少 操作数。
#
# 如果 x == 2i 且其中 i >= 0 ，则数字 x 是 2 的幂。
#
#
#
# 示例 1：
#
# 输入：n = 39
# 输出：3
# 解释：我们可以执行下述操作：
# - n 加上 20 = 1 ，得到 n = 40 。
# - n 减去 23 = 8 ，得到 n = 32 。
# - n 减去 25 = 32 ，得到 n = 0 。
# 可以证明使 n 等于 0 需要执行的最少操作数是 3 。
# 示例 2：
#
# 输入：n = 54
# 输出：3
# 解释：我们可以执行下述操作：
# - n 加上 21 = 2 ，得到 n = 56 。
# - n 加上 23 = 8 ，得到 n = 64 。
# - n 减去 26 = 64 ，得到 n = 0 。
# 使 n 等于 0 需要执行的最少操作数是 3 。
#
#
# 提示：
#
# 1 <= n <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, n: int) -> int:
        # b = bin(n)[2:]
        # print(b)
        # cnt0, cnt1 = b.count('0'), b.count('1')
        # return min(cnt0 + 2, cnt1)
        ex = [-1] * (n * 2 + 2)
        q = [1]
        while q[-1] * 2 <= n * 2:
            q.append(q[-1] * 2)
        mi = [x for x in q]
        q = deque(q)
        step = 1
        while len(q):
            qq = deque([])
            while len(q):
                x = q.popleft()
                ex[x] = step
                if x == n:
                    return step
                for y in mi:
                    if x + y < len(ex) and ex[x + y] == -1:
                        qq.append(x + y)
                        ex[x + y] = 0
                    if x > y and ex[x - y] == -1:
                        qq.append(x - y)
                        ex[x - y] = 0
            step += 1
            q = qq
            # print(ex[64])



so = Solution()
print(so.minOperations(56))  # 2
print(so.minOperations(40))  # 2
print(so.minOperations(39))  # 3
print(so.minOperations(27))  # 3
print(so.minOperations(38))
print(so.minOperations(54))  # 3




