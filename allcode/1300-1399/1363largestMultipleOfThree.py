# 给你一个整数数组 digits，你可以通过按 任意顺序 连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
#
# 由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。如果无法得到答案，请返回一个空字符串。返回的结果不应包含不必要的前导零。
#
#
#
# 示例 1：
#
# 输入：digits = [8,1,9]
# 输出："981"
# 示例 2：
#
# 输入：digits = [8,6,7,1,0]
# 输出："8760"
# 示例 3：
#
# 输入：digits = [1]
# 输出：""
# 示例 4：
#
# 输入：digits = [0,0,0,0,0,0]
# 输出："0"
#
#
# 提示：
#
# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dp0, dp1, dp2 = [0] * 10, [0] * 10, [0] * 10  # dpi表示前j-1个数构成的模3余数为i的最大数字(以Counter的形式记录)

        def trans(c):
            ans = []
            for i in range(9, -1, -1):
                ans += [str(i)] * c[i]
            if len(ans) == 0 or ans[0] == '0':
                return '0'
            return ''.join(ans)
        def MAX(c1, c2):
            a, b = trans(c1), trans(c2)
            if len(a) < len(b):
                return c2
            if len(a) > len(b):
                return c1
            if a < b:
                return c2
            return c1
        # 三个标记，记录三个dp数组是否有效
        # 其中v0是一定有效的，因为一个数字都没有处理时，就是0，是3的倍数
        v0 = True
        v1 = v2 = False
        for x in digits:
            ndp0, ndp1, ndp2 = dp0[:], dp1[:], dp2[:]
            if v0:
                ndp0[x] += 1
            if v1:
                ndp1[x] += 1
            if v2:
                ndp2[x] += 1
            if x % 3 == 0:
                dp0, dp1, dp2 = ndp0, ndp1, ndp2
            elif x % 3 == 1:
                if v2:
                    dp0 = MAX(dp0, ndp2)
                dp1 = MAX(dp1, ndp0)
                if v1:
                    dp2 = MAX(dp2, ndp1)
                    v2 = True
                v1 = True  # v0一定是有效的
            elif x % 3 == 2:
                if v1:
                    dp0 = MAX(dp0, ndp1)
                if v2:
                    dp1 = MAX(dp1, ndp2)
                    v1 = True
                dp2 = MAX(dp2, ndp0)
                v2 = True  # v0一定是有效的

        return trans(dp0)



so = Solution()
print(so.largestMultipleOfThree([1]))
print(so.largestMultipleOfThree([8,1,9]))
print(so.largestMultipleOfThree([8,6,7,1,0]))
print(so.largestMultipleOfThree([0,0,0,0,0,0]))




