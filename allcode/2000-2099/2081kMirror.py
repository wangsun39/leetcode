# 一个 k 镜像数字 指的是一个在十进制和 k 进制下从前往后读和从后往前读都一样的 没有前导 0 的 正 整数。
#
# 比方说，9 是一个 2 镜像数字。9 在十进制下为 9 ，二进制下为 1001 ，两者从前往后读和从后往前读都一样。
# 相反地，4 不是一个 2 镜像数字。4 在二进制下为 100 ，从前往后和从后往前读不相同。
# 给你进制 k 和一个数字 n ，请你返回 k 镜像数字中 最小 的 n 个数 之和 。
#
#
#
# 示例 1：
#
# 输入：k = 2, n = 5
# 输出：25
# 解释：
# 最小的 5 个 2 镜像数字和它们的二进制表示如下：
#   十进制       二进制
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# 它们的和为 1 + 3 + 5 + 7 + 9 = 25 。
# 示例 2：
#
# 输入：k = 3, n = 7
# 输出：499
# 解释：
# 7 个最小的 3 镜像数字和它们的三进制表示如下：
#   十进制       三进制
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# 它们的和为 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499 。
# 示例 3：
#
# 输入：k = 7, n = 17
# 输出：20379000
# 解释：17 个最小的 7 镜像数字分别为：
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
#
#
# 提示：
#
# 2 <= k <= 9
# 1 <= n <= 30

from leetcode.allcode.competition.mypackage import *

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        l = 1  # 表示数字长度
        def trans(x):
            res = []
            while x:
                q, r = divmod(x, k)
                x = q
                res.append(str(r))
            return ''.join(res[::-1])
        ans = 0
        while n:
            if l & 1:
                for i in range(10 ** ((l + 1) // 2 - 1), 10 ** ((l + 1) // 2)):
                    if i >= 10:
                        j = int(str(i) + str(i // 10)[::-1])
                    else:
                        j = int(str(i))
                    kj = trans(j)
                    if kj == kj[::-1]:
                        ans += j
                        n -= 1
                        if n == 0:
                            return ans
            else:
                for i in range(10 ** (l // 2 - 1), 10 ** (l // 2)):
                    j = int(str(i) + str(i)[::-1])
                    kj = trans(j)
                    if kj == kj[::-1]:
                        ans += j
                        n -= 1
                        if n == 0:
                            return ans
            l += 1
        return ans


so = Solution()
print(so.kMirror(k = 3, n = 7))
print(so.kMirror(k = 2, n = 5))
print(so.kMirror(k = 7, n = 17))




