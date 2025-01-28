# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字1和0。
#
# 
#
# 示例1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#
# 提示：
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        N1, N2 = len(a), len(b)
        if N1 > N2:
            a, b, N1, N2 = b, a, N2, N1
        a = '0' * (N2 - N1) + a
        carry = 0
        res = ''
        for i in range(N2 - 1, -1, -1):
            if a[i] == b[i]:
                c = '1' if 1 == carry else '0'
                carry = 1 if b[i] == '1' else 0
            else:
                c = '0' if 1 == carry else '1'
            res = c + res

        return '1' + res if 1 == carry else res


so = Solution()
print(so.addBinary("11", "1"))  # 100
print(so.addBinary("1010", "1011"))  # 10101


