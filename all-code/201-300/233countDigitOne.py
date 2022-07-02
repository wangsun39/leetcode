# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#  
#
# 示例 1：
#
# 输入：n = 13
# 输出：6
# 示例 2：
#
# 输入：n = 0
# 输出：0
#  
#
# 提示：
#
# 0 <= n <= 109


class Solution:
    def countDigitOne(self, n: int) -> int:
        oneNum = [i * pow(10, i - 1) for i in range(10)]  # oneNum[i] 表示小于i+1位数的数中有多少个1，比如 oneNum[1] 小于2位数的所有数有几个1
        # print(oneNum)
        string = str(n)
        length = len(string)
        res = 0
        for i in range(length):
            digit = int(string[i])
            ds = length - i  # 表示当前数字是第几位数
            if digit == 1:
                if i + 1 == length:  # 最后一位
                    res += 1
                else:
                    res += int(string[i + 1:]) + 1 + oneNum[ds - 1] # 比如 1200，int(string[i + 1:])表示1000-1200在千位上有201个1，oneNum[ds - 1]表示[0,999]有多个1
            elif digit == 0:
                continue
            else:
                res += oneNum[ds - 1] * digit + pow(10, ds - 1)
            # print(res)
        return int(res)




so = Solution()
print(so.countDigitOne(10))
print(so.countDigitOne(0))
print(so.countDigitOne(11))
print(so.countDigitOne(13))



