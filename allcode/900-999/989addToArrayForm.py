# 整数的 数组形式  num 是按照从左到右的顺序表示其数字的数组。
#
# 例如，对于 num = 1321 ，数组形式是 [1,3,2,1] 。
# 给定 num ，整数的 数组形式 ，和整数 k ，返回 整数 num + k 的 数组形式 。
#
#
#
# 示例 1：
#
# 输入：num = [1,2,0,0], k = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
# 示例 2：
#
# 输入：num = [2,7,4], k = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
# 示例 3：
#
# 输入：num = [2,1,5], k = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
#
#
# 提示：
#
# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num 不包含任何前导零，除了零本身
# 1 <= k <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        k = list(str(k))[::-1]
        mx = max(len(num), len(k))
        num += [0] * (mx - len(num))
        k += [0] * (mx - len(k))
        ans = [0] * mx
        carry = 0
        for i in range(mx):
            ans[i] = num[i] + int(k[i]) + carry
            carry = ans[i] > 9
            ans[i] %= 10
        if carry:
            ans.append(1)
        ans.reverse()
        return ans



so = Solution()
print(so.addToArrayForm(num = [1,2,0,0], k = 34))




