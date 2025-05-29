# 为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 arrayA 记录了各个生物群体数量数据，其中 arrayA[i] 表示第 i 个生物群体的数量。请返回一个数组 arrayB，该数组为基于数组 arrayA 中的数据计算得出的结果，其中 arrayB[i] 表示将第 i 个生物群体的数量从总体中排除后的其他数量的乘积。
#
#
#
# 示例 1：
#
# 输入：arrayA = [2, 4, 6, 8, 10]
# 输出：[1920, 960, 640, 480, 384]
#
#
# 提示：
#
# 所有元素乘积之和不会溢出 32 位整数
# arrayA.length <= 100000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        n = len(arrayA)
        if n == 0: return arrayA
        c0 = arrayA.count(0)
        if c0 > 1:
            return [0] * n
        if c0 == 0:
            m = reduce(lambda x, y: x * y, arrayA)
            return [m // x for x in arrayA]
        m = 1
        for x in arrayA:
            if x:
                m *= x
        return [m if x == 0 else 0 for x in arrayA]


so = Solution()




