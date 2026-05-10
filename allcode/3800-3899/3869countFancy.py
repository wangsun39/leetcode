# 给你两个整数 l 和 r。

# 如果一个整数的数位形成一个 严格单调 序列，即数位是 严格递增 或 严格递减 的，那么这个整数被称为 好数。所有一位数都被认为是好数。
#
# 如果一个整数是好数，或者它的 数位和 是好数，那么这个整数被称为 奇妙数。
#
# 返回一个整数，表示在区间 [l, r]（包含边界）内的奇妙数的数量。
#
# 如果一个序列中的每个元素都 严格大于 其前一个元素（如果存在），则该序列被称为 严格递增。
#
# 如果一个序列中的每个元素都 严格小于 其前一个元素（如果存在），则该序列被称为 严格递减。
#
#
#
# 示例 1：
#
# 输入： l = 8, r = 10
#
# 输出： 3
#
# 解释：
#
# 8 和 9 是一位数，所以它们是好数，因此也是奇妙数。
# 10 的数位为 [1, 0]，形成了一个严格递减的序列，所以 10 是好数，因此也是奇妙数。
# 因此，答案是 3。
#
# 示例 2：
#
# 输入： l = 12340, r = 12341
#
# 输出： 1
#
# 解释：
#
# 12340
# 12340 不是好数，因为 [1, 2, 3, 4, 0] 不是严格单调的。
# 数位和为 1 + 2 + 3 + 4 + 0 = 10。
# 10 是好数，因为它的数位为 [1, 0]，是严格递减的。因此，12340 是奇妙数。
# 12341
# 12341 不是好数，因为 [1, 2, 3, 4, 1] 不是严格单调的。
# 数位和为 1 + 2 + 3 + 4 + 1 = 11。
# 11 不是好数，因为它的数位为 [1, 1]，不是严格单调的。因此，12341 不是奇妙数。
# 因此，答案是 1。
#
# 示例 3：
#
# 输入： l = 123456788, r = 123456788
#
# 输出： 0
#
# 解释：
#
# 123456788 不是好数，因为它的数位不是严格单调的。
# 数位和为 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8 = 44。
# 44 不是好数，因为它的数位为 [4, 4]，不是严格单调的。因此，123456788 不是奇妙数。
# 因此，答案是 0。
#
#
#
# 提示：
#
# 1 <= l <= r <= 1015

from leetcode.allcode.competition.mypackage import *

sum_good = set(range(10))  # 数位和是好数的数位和
for i in range(10, 15 * 9 + 1):
    si = str(i)
    if len(si) == 2:
        if si[0] != si[1]:
            sum_good.add(i)
    else:
        if  si[0] < si[1] < si[2] or si[0] > si[1] > si[2]:
            sum_good.add(i)


class Solution:
    def countFancy(self, l: int, r: int) -> int:

        def f(num: str):  # 数字 <= num 满足条件的所有数字
            if int(num) < 10:
                return int(num) + 1

            @cache
            def digitDp(i: int, is_limit: bool, pre: int, st: int, s: int) -> int:
                # st 表示状态0: 初始，1: 上升， 2: 下降， 3: 乱序
                if i == len(num):
                    return st in (1, 2) or s in sum_good
                ans = 0
                upper = int(num[i]) if is_limit else 9  # 判断当前位是否受约束
                for j in range(upper + 1):
                    if st == 0 and pre == 0:
                        new_st = 0
                    elif st in (0, 1) and pre < j:
                        new_st = 1
                    elif st in (0, 2) and pre > j:
                        new_st = 2
                    else:
                        new_st = 3
                    ans += digitDp(i + 1, is_limit and j == upper, j, new_st, s + j)
                return ans
            return digitDp(0, True, 0, 0, 0)

        num1 = str(int(l) - 1)
        return f(str(r)) - f(num1)



so = Solution()
print(so.countFancy(l = 1, r = 100))
print(so.countFancy(l = 8, r = 10))




