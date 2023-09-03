# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
#
#  
#
# 示例 1:
#
# 输入: num = 100
# 输出: "202"
# 示例 2:
#
# 输入: num = -7
# 输出: "-10"
#  
#
# 提示：
#
# -107 <= num <= 107


import bisect

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        flag = ''
        if num < 0:
            flag = '-'
            num = -num
        while num > 0:
            res += str(num % 7)
            num //= 7
        return flag + res[::-1]



so = Solution()
print(so.convertToBase7(100))
print(so.convertToBase7(-7))

