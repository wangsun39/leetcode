# 给你一个整数 n。
#
# 如果一个整数的二进制表示中所有位都相同，则称其为 单比特数（Monobit）。
#
# 返回范围[0, n]（包括两端）内 单比特数 的个数。
#
#
#
# 示例 1：
#
# 输入： n = 1
#
# 输出： 2
#
# 解释：
#
# 范围[0, 1]内的整数对应的二进制表示为"0"和"1"。
# 每个表示都由相同的位组成，因此答案是2。
# 示例 2：
#
# 输入： n = 4
#
# 输出： 3
#
# 解释：
#
# 范围[0, 4]内的整数对应的二进制表示为"0"、"1"、"10"、"11"和"100"。
# 只有0、1和3满足单比特条件。因此答案是3。
#
#
# 提示：
#
# 0 <= n <= 1000

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(20):
            if (1 << i) - 1 <= n:
                ans += 1
            else:
                break
        return ans


so = Solution()
print(so.countMonobit(7))
print(so.countMonobit(4))
print(so.countMonobit(1))




