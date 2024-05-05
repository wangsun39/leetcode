# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
#
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#
#
#
# 示例 1：
#
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 示例 2：
#
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
#
#
# 提示：
#
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
from leetcode.allcode.competition.mypackage import *

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        c = [[k, v] for k, v in counter.items()]
        c.sort(key=lambda x: -x[1])
        n = len(barcodes)
        ans = [0] * n
        j = 0
        for i in range(0, n, 2):
            ans[i] = c[j][0]
            c[j][1] -= 1
            if c[j][1] == 0:
                j += 1
        for i in range(1, n, 2):
            ans[i] = c[j][0]
            c[j][1] -= 1
            if c[j][1] == 0:
                j += 1
        return ans




so = Solution()
print(so.rearrangeBarcodes([1,1,1,2,2,2]))
print(so.rearrangeBarcodes([1,1,1,1,2,2,3,3]))


