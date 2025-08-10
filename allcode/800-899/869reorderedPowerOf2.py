# 给定正整数 n ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：true
# 示例 2：
#
# 输入：n = 10
# 输出：false
#
#
# 提示：
#
# 1 <= n <= 109


from leetcode.allcode.competition.mypackage import *

p2 = [1 << i for i in range(32)]
sp2 = set()
for x in p2:
    sx = list(str(x))
    sx.sort(reverse=True)
    sp2.add(tuple(sx))

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sn = tuple(sorted(list(str(n)), reverse=True))
        return sn in sp2




so = Solution()
print(so.reorderedPowerOf2(10))

