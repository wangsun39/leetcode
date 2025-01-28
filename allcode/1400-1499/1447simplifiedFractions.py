# 给你一个整数n，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于n的 最简分数。分数可以以 任意顺序返回。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
# 示例 2：
#
# 输入：n = 3
# 输出：["1/2","1/3","2/3"]
# 示例 3：
#
# 输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
# 示例 4：
#
# 输入：n = 1
# 输出：[]
#
#
# 提示：
#
# 1 <= n <= 100



from typing import List
import math

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        factors = [set() for _ in range(n + 1)]
        def getAllFactor(n):
            s = set()
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    s.add(i)
                    s.add(n // i)
            return s
        for i in range(2, n + 1):
            factors[i] = getAllFactor(i)
        print(factors)
        res = []
        def getAllNumerator(n):
            res = [1]
            for i in range(1, n):
                if len(factors[i] & factors[n]) == 0 and n % i != 0:
                    res.append(i)
            return res
        for i in range(2, n + 1):
            numerator = getAllNumerator(i)
            print(i, numerator)
            for j in numerator:
                res.append(str(j) + '/' + str(i))
        return res



so = Solution()
print(so.simplifiedFractions(4))




