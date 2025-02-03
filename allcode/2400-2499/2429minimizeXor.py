# 给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：
#
# x 的置位数和 num2 相同，且
# x XOR num1 的值 最小
# 注意 XOR 是按位异或运算。
#
# 返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。
#
# 整数的 置位数 是其二进制表示中 1 的数目。
#
#
#
# 示例 1：
#
# 输入：num1 = 3, num2 = 5
# 输出：3
# 解释：
# num1 和 num2 的二进制表示分别是 0011 和 0101 。
# 整数 3 的置位数与 num2 相同，且 3 XOR 3 = 0 是最小的。
# 示例 2：
#
# 输入：num1 = 1, num2 = 12
# 输出：3
# 解释：
# num1 和 num2 的二进制表示分别是 0001 和 1100 。
# 整数 3 的置位数与 num2 相同，且 3 XOR 1 = 2 是最小的。
#
#
# 提示：
#
# 1 <= num1, num2 <= 109
#
# https://leetcode.cn/problems/minimize-xor

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count(x):
            res = 0
            while x:
                x &= (x - 1)
                res += 1
            return res
        count1, count2 = count(num1), count(num2)
        # l1, l2 = num1.bit_count(), num2.bit_count()
        s1 = bin(num1)[2:]
        s2 = ''
        if count1 >= count2:
            cnt = 0
            for s in s1:
                if cnt >= count2:
                    s2 += ('0' * (len(s1) - len(s2)))
                    break
                if s == '1':
                    s2 += '1'
                    cnt += 1
                else:
                    s2 += '0'
        elif count2 >= len(s1):
            return int('1' * count2, 2)
        else:
            cnt = 0
            for s in s1:
                if cnt >= count1:
                    delta = min(count2 - count1, len(s1) - len(s2))
                    s2 = s2 + ('0' * (len(s1) - len(s2) - delta)) + ('1' * delta)
                    break
                if s == '1':
                    s2 += '1'
                    cnt += 1
                else:
                    s2 += '0'
            if s2.count('1') < count2:
                delta = count2 - s2.count('1')
                while delta > 0:
                    pos = s2.rfind('0')
                    s2 = s2[:pos] + '1' + s2[pos + 1:]
                    delta -= 1
        print(s2)

        return int(s2, 2)



so = Solution()
print(so.minimizeXor(num1 = 3756, num2 = 7038))
print(so.minimizeXor(num1 = 65, num2 = 84))
print(so.minimizeXor(num1 = 1, num2 = 12))
print(so.minimizeXor(num1 = 3, num2 = 5))
print(so.minimizeXor(num1 = 8, num2 = 3))




