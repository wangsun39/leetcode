# 给你三个整数 n、pos 和 k。
#

# 有 n 个人排成一排，下标从 0 到 n - 1。每个人 独立地 选择一个方向：
#
# 'L'：只对他们 右边 的人 可见
# 'R'：只对他们 左边 的人 可见
# 位于下标 pos 的人看其他人的方式如下：
# 一个 i < pos 的人可见当且仅当他们选择 'L'。
# 一个 i > pos 的人可见当且仅当他们选择 'R'。
# 返回可能的方向分配数量，使得位于下标 pos 的人 恰好 看到 k 个人。
#
# 由于答案可能很大，请将其对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入： n = 3, pos = 1, k = 0
#
# 输出： 2
#
# 解释：
#
# 下标 0 在 pos = 1 的左侧，下标 2 在 pos = 1 的右侧。
# 为了看到 k = 0 个人，下标 0 必须选择 'R'，且下标 2 必须选择 'L'，这样两人都不可见。
# 位于下标 1 的人可以选择 'L' 或 'R'，因为这不会影响计数。因此，答案是 2。
# 示例 2：
#
# 输入： n = 3, pos = 2, k = 1
#
# 输出： 4
#
# 解释：
#
# 下标 0 和下标 1 在 pos = 2 的左侧，右侧没有下标。
# 为了看到 k = 1 个人，下标 0 或下标 1 中必须恰好有一个选择 'L'，另一个必须选择 'R'。
# 有 2 种方法可以选择哪个下标从左侧可见。
# 位于下标 2 的人可以选择 'L' 或 'R'，因为这不会影响计数。因此，答案是 2 + 2 = 4。
# 示例 3：
#
# 输入： n = 1, pos = 0, k = 0
#
# 输出： 2
#
# 解释：
#
# pos = 0 的左侧或右侧没有下标。
# 为了看到 k = 0 个人，不需要额外的条件。
# 位于下标 0 的人可以选择 'L' 或 'R'。因此，答案是 2。
#
#
# 提示：
#
# 1 <= n <= 105
# 0 <= pos, k <= n - 1

from leetcode.allcode.competition.mypackage import *

MOD = 1_000_000_007
MX = 100_000

f = [0] * MX  # f[i] = i!
f[0] = 1
for i in range(1, MX):
    f[i] = f[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(f[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

def comb(n: int, m: int) -> int:
    return f[n] * inv_f[m] * inv_f[n - m] % MOD

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return comb(n - 1, k) * 2 % MOD



so = Solution()




