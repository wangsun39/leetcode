# 给你两个整数 num1 和 num2，表示一个 闭 区间 [num1, num2]。
#
# 一个数字的 波动值 定义为该数字中 峰 和 谷 的总数：
#
# 如果一个数位 严格大于 其两个相邻数位，则该数位为 峰。
# 如果一个数位 严格小于 其两个相邻数位，则该数位为 谷。
# 数字的第一个和最后一个数位 不能 是峰或谷。
# 任何少于 3 位的数字，其波动值均为 0。
# 返回范围 [num1, num2] 内所有数字的波动值之和。
#
#
# 示例 1：
#
# 输入： num1 = 120, num2 = 130
#
# 输出： 3
#
# 解释：
#
# 在范围 [120, 130] 内：
#
# 120：中间数位 2 是峰，波动值 = 1。
# 121：中间数位 2 是峰，波动值 = 1。
# 130：中间数位 3 是峰，波动值 = 1。
# 范围内所有其他数字的波动值均为 0。
# 因此，总波动值为 1 + 1 + 1 = 3。
#
# 示例 2：
#
# 输入： num1 = 198, num2 = 202
#
# 输出： 3
#
# 解释：
#
# 在范围 [198, 202] 内：
#
# 198：中间数位 9 是峰，波动值 = 1。
# 201：中间数位 0 是谷，波动值 = 1。
# 202：中间数位 0 是谷，波动值 = 1。
# 范围内所有其他数字的波动值均为 0。
# 因此，总波动值为 1 + 1 + 1 = 3。
#
# 示例 3：
#
# 输入： num1 = 4848, num2 = 4848
#
# 输出： 2
#
# 解释：
#
# 数字 4848：第二个数位 8 是峰，第三个数位 4 是谷，波动值为 2。
#
#
#
# 提示：
#
# 1 <= num1 <= num2 <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # n = len(str(num2))

        def f(num: str):  # 数字 <= num 满足条件的所有数字
            @cache
            def digitDp(i: int, pre_dir: int, pre: int, seq: int, is_limit: bool) -> int:
                # 枚举第i位，i-1位值为pre， i-2位与i-1位的大小关系pre_dir(-1,0,1,2)  2表示前面不足2个数字
                # 从0到i-1的的波谷个数为 seq
                if i == len(num):
                    return seq
                ans = 0
                if pre == -1: # 未构成数字
                    ans = digitDp(i + 1, 2, -1, seq, False)
                upper = int(num[i]) if is_limit else 9  # 判断当前位是否受约束
                lower = 0 if pre != -1 else 1
                for j in range(lower, upper + 1): # 枚举当前位数字
                    if pre == -1:  # 前面没有数字
                        ans += digitDp(i + 1, 2, j, seq, is_limit and j == upper)
                    else:
                        if j == pre:
                            dir = 0
                        elif pre < j:
                            dir = -1
                        else:
                            dir = 1
                        if pre_dir == 2:
                            ans += digitDp(i + 1, dir, j, seq, is_limit and j == upper)
                        else:
                            if (pre_dir == -1 and dir == 1) or (pre_dir == 1 and dir == -1):
                                ans += digitDp(i + 1, dir, j, seq + 1, is_limit and j == upper)
                            else:
                                ans += digitDp(i + 1, dir, j, seq, is_limit and j == upper)

                return ans

            return digitDp(0, 2, -1, 0, True)

        return f(str(num2)) - f(str(num1 - 1))



so = Solution()
print(so.totalWaviness(num1 = 1201, num2 = 1201))
print(so.totalWaviness(num1 = 120, num2 = 130))




