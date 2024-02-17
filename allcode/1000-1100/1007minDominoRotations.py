# 在一排多米诺骨牌中，tops[i] 和 bottoms[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）
#
# 我们可以旋转第 i 张多米诺，使得 tops[i] 和 bottoms[i] 的值交换。
#
# 返回能使 tops 中所有值或者 bottoms 中所有值都相同的最小旋转次数。
#
# 如果无法做到，返回 -1.
#
#
#
# 示例 1：
#
#
# 输入：tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# 输出：2
# 解释：
# 图一表示：在我们旋转之前， tops 和 bottoms 给出的多米诺牌。
# 如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
# 示例 2：
#
# 输入：tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# 输出：-1
# 解释： 在这种情况下，不可能旋转多米诺牌使一行的值相等。
#
#
# 提示：
#
# 2 <= tops.length <= 2 * 104
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def count(istop, num):
            res = 0
            for i in range(n):
                if istop:
                    if tops[i] == num:
                        continue
                    if bottoms[i] == num:
                        res += 1
                        continue
                else:
                    if bottoms[i] == num:
                        continue
                    if tops[i] == num:
                        res += 1
                        continue
                return inf
            return res
        r1 = count(True, tops[0])
        r2 = count(True, bottoms[0])
        r3 = count(False, tops[0])
        r4 = count(False, bottoms[0])
        r = min(r1, r2, r3, r4)
        if r == inf:
            return -1
        return r


so = Solution()
print(so.minDominoRotations([1,2,1,1,1,2,2,2],
[2,1,2,2,2,2,2,2]))
print(so.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
print(so.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))




