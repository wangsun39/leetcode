# 给你一组多米诺骨牌 dominoes 。
#
# 形式上，dominoes[i] = [a, b] 与 dominoes[j] = [c, d] 等价 当且仅当 (a == c 且 b == d) 或者 (a == d 且 b == c) 。即一张骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌。
#
# 在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
#
#
#
# 示例 1：
#
# 输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
# 输出：1
# 示例 2：
#
# 输入：dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# 输出：3
#
#
# 提示：
#
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numEquivDominoPairs1(self, dominoes):
        def equal(a, b):
            if (a[0] == b[0] and a[1] == b[1]) or (a[1] == b[0] and a[0] == b[1]):
                return True
            return False
        nums = len(dominoes)
        res = 0
        while len(dominoes) > 1:
            nums = len(dominoes)
            sum_D0 = 1 # 与第0个domino相同的domino个数(包括第0个)
            for l2 in range(nums-1, 0, -1):
                if equal(dominoes[0], dominoes[l2]):
                    sum_D0 += 1
                    dominoes.pop(l2)
            res += (sum_D0 * (sum_D0-1) // 2)
            dominoes.pop(0)
        return res


    def numEquivDominoPairs(self, dominoes):
        # 2025/5/4 hash counter
        counter = Counter()
        ans = 0
        for x, y in dominoes:
            if (x, y) in counter:
                ans += counter[(x, y)]
                counter[(x, y)] += 1
            else:
                ans += counter[(y, x)]
                counter[(y, x)] += 1
        return ans


obj = Solution()
print(obj.numEquivDominoPairs([[1,2]]))
print(obj.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))

