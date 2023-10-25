# 给你一个正整数 n ，请你返回 n 的 惩罚数 。
#
# n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：
#
# 1 <= i <= n
# i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。
#
#
# 示例 1：
#
# 输入：n = 10
# 输出：182
# 解释：总共有 3 个整数 i 满足要求：
# - 1 ，因为 1 * 1 = 1
# - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
# - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
# 因此，10 的惩罚数为 1 + 81 + 100 = 182
# 示例 2：
#
# 输入：n = 37
# 输出：1478
# 解释：总共有 4 个整数 i 满足要求：
# - 1 ，因为 1 * 1 = 1
# - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
# - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
# - 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
# 因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478
#
#
# 提示：
#
# 1 <= n <= 1000
from leetcode.allcode.competition.mypackage import *


class Solution1:
    def punishmentNumber(self, n: int) -> int:
        def check(x):  # 检查 x * x 是否满足条件
            y = str(x * x)
            m = len(y)
            def dfs(i, t):  # 从i位开始向后，目标为t
                if i == m: return t == 0
                for j in range(m - i):
                    seg = y[i: i + j + 1]
                    if int(seg) > t:
                        break
                    if dfs(i + j + 1, t - int(seg)):
                        return True
                return False
            return dfs(0, x)
        ans = 0
        for i in range(1, n + 1):
            if check(i):
                ans += i * i
        return ans


# 2023/10/25  预处理 + 记忆化搜索
@cache
def find(s, t): # 字符串s是否能分割成几段，他们之和为t
    if t < 0 or len(s) == 0: return False
    if int(s) == t:
        return True
    if len(s) == 1:
        return int(s) == t
    for i in range(len(s)):
        if find(s[i + 1:], t - int(s[:i + 1])):
            return True
    return False

def check(x):
    s = str(x * x)
    return find(s, x)

s = set()
for i in range(1, 1001):
    if check(i):
        s.add(i)
# print(s)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(x * x for x in range(1, n + 1) if x in s)

so = Solution()
print(so.punishmentNumber(10))
print(so.punishmentNumber(37))
print(so.punishmentNumber(45))




