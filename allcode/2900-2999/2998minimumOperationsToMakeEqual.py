# 给你两个正整数 x 和 y 。
#
# 一次操作中，你可以执行以下四种操作之一：
#
# 如果 x 是 11 的倍数，将 x 除以 11 。
# 如果 x 是 5 的倍数，将 x 除以 5 。
# 将 x 减 1 。
# 将 x 加 1 。
# 请你返回让 x 和 y 相等的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：x = 26, y = 1
# 输出：3
# 解释：我们可以通过以下操作将 26 变为 1 ：
# 1. 将 x 减 1
# 2. 将 x 除以 5
# 3. 将 x 除以 5
# 将 26 变为 1 最少需要 3 次操作。
# 示例 2：
#
# 输入：x = 54, y = 2
# 输出：4
# 解释：我们可以通过以下操作将 54 变为 2 ：
# 1. 将 x 加 1
# 2. 将 x 除以 11
# 3. 将 x 除以 5
# 4. 将 x 加 1
# 将 54 变为 2 最少需要 4 次操作。
# 示例 3：
#
# 输入：x = 25, y = 30
# 输出：5
# 解释：我们可以通过以下操作将 25 变为 30 ：
# 1. 将 x 加 1
# 2. 将 x 加 1
# 3. 将 x 加 1
# 4. 将 x 加 1
# 5. 将 x 加 1
# 将 25 变为 30 最少需要 5 次操作。
#
#
# 提示：
#
# 1 <= x, y <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        d = {x: 0}
        dq1 = deque([x])
        if x == y: return 0
        i = 0
        while dq1:
            i += 1
            dq2 = deque()
            while dq1:
                x = dq1.popleft()
                if 0 < x + 1 <= 10000 and x + 1 not in d:
                    if x + 1 == y:
                        return i
                    d[x + 1] = i
                    dq2.append(x + 1)
                if 0 < x - 1 <= 10000 and x - 1 not in d:
                    if x - 1 == y:
                        return i
                    d[x - 1] = i
                    dq2.append(x - 1)
                if x % 5 == 0 and x // 5 not in d:
                    if x // 5 == y:
                        return i
                    d[x // 5] = i
                    dq2.append(x // 5)
                if x % 11 == 0 and x // 11 not in d:
                    if x // 11 == y:
                        return i
                    d[x // 11] = i
                    dq2.append(x // 11)
            dq1 = dq2




so = Solution()
print(so.minimumOperationsToMakeEqual(x = 25, y = 30))
print(so.minimumOperationsToMakeEqual(x = 26, y = 1))
print(so.minimumOperationsToMakeEqual(x = 54, y = 2))




