# 返回所有长度为 n 且满足其每两个连续位上的数字之间的差的绝对值为 k 的 非负整数 。
#
# 请注意，除了 数字 0 本身之外，答案中的每个数字都 不能 有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 3, k = 7
# 输出：[181,292,707,818,929]
# 解释：注意，070 不是一个有效的数字，因为它有前导零。
# 示例 2：
#
# 输入：n = 2, k = 1
# 输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 示例 3：
#
# 输入：n = 2, k = 0
# 输出：[11,22,33,44,55,66,77,88,99]
# 示例 4：
#
# 输入：n = 2, k = 2
# 输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
#
#
# 提示：
#
# 2 <= n <= 9
# 0 <= k <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []

        @cache
        def dfs(pos, v):
            if pos == n - 1:
                return [[v]]
            res = []
            if v + k < 10:
                arr = dfs(pos + 1, v + k)
                res = [[v] + x for x in arr]
            if v - k >= 0 and k:
                arr = dfs(pos + 1, v - k)
                res += [[v] + x for x in arr]
            return res

        for start in range(1, 10):
            ans += dfs(0, start)

        ans = [[str(x) for x in y] for y in ans]
        ans = [int(''.join(x)) for x in ans]
        return ans



so = Solution()
print(so.numsSameConsecDiff(n = 3, k = 7))
