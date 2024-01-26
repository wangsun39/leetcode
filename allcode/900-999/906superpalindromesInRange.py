# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
#
# 现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
#
#
#
# 示例：
#
# 输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及 484 是超级回文数。
# 注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
#
#
# 提示：
#
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
# int(L) <= int(R)

from leetcode.allcode.competition.mypackage import *

def check(x):
    return str(x) == str(x)[::-1]
sp = set()
for i in range(1, 50001):
    a = str(i) + str(i)[::-1]
    b = str(i) + str(i)[:-1][::-1]
    ai, bi = int(a), int(b)
    ai2, bi2 = ai ** 2, bi ** 2
    if check(ai2):
        sp.add(ai2)
    if check(bi2):
        sp.add(bi2)
sp = list(sp)
sp.sort()


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l, r = int(left), int(right)
        return bisect_right(sp, r) - bisect_left(sp, l)


so = Solution()
print(so.superpalindromesInRange("4", "1000"))




