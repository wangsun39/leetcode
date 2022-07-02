# 两数之和
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        # 采用2进制竖式除法
        abs_m = abs(dividend)
        abs_n = abs(divisor)
        if abs_m < abs_n:
            return 0
        if (abs_n == divisor) == (abs_m == dividend):
            # 符合相同
            sign = 1
        else:
            sign = -1
        tmp_n = abs_n
        h = 0  # n要左移多少位才能开始除法，如：1010111 / 101 要将101左移4位，成为1010000开始相除
        while (tmp_n << 1) <= abs_m:
            tmp_n = tmp_n << 1
            h += 1
        cur_m, cur_n = abs_m, abs_n
        result = 0
        while h >= 0:
            cur_n = (abs_n << h)
            if cur_m > cur_n:
                result = result + (1 << h)
                cur_m = cur_m - cur_n
                h -= 1
            elif cur_m == cur_n:
                result = result + (1 << h)
                break
            else:
                h -= 1
        result = result if sign == 1 else -result
        return result - 1 if result == 2147483648 else result



so = Solution()
#print(so.divide(15, 3), 5 == so.divide(15, 3))
#print(so.divide(15, 2), 7 == so.divide(15, 2))
#print(so.divide(-15, 2), -7 == so.divide(-15, 2))
print(so.divide(-4, 1), -4 == so.divide(-4, 1))
# print(so.twoSum([2,7,11,15],9))
# print(so.twoSum_Hash([2,7,11,15],9))
