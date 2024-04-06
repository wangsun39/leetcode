# 给你一个整数 num，请你找出同时满足下面全部要求的两个整数：
#
# 两数乘积等于  num + 1 或 num + 2
# 以绝对差进行度量，两数大小最接近
# 你可以按任意顺序返回这两个整数。
#
#
#
# 示例 1：
#
# 输入：num = 8
# 输出：[3,3]
# 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。
# 示例 2：
#
# 输入：num = 123
# 输出：[5,25]
# 示例 3：
#
# 输入：num = 999
# 输出：[40,25]
#
#
# 提示：
#
# 1 <= num <= 10^9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def factors(x):
            res = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    res.append(i)
                    last = i
                i += 1
            return [last, x // last]  # 最后一次加入的就是最接近的一对
        a, b = factors(num + 1)
        c, d = factors(num + 2)
        if b - a < d - c:
            return [a, b]
        return [c, d]



so = Solution()
print(so.closestDivisors(8))
print(so.closestDivisors(123))
print(so.closestDivisors(999))




