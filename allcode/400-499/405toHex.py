# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
#
# 答案字符串中的所有字母都应该是小写字符，并且除了 0 本身之外，答案中不应该有任何前置零。
#
# 注意: 不允许使用任何由库提供的将数字直接转换或格式化为十六进制的方法来解决这个问题。
#
#
#
# 示例 1：
#
# 输入：num = 26
# 输出："1a"
# 示例 2：
#
# 输入：num = -1
# 输出："ffffffff"
#
#
# 提示：
#
# -231 <= num <= 231 - 1



class Solution:
    def toHex(self, num: int) -> str:
        s = []
        for i in range(8):
            s.append(num & 0xF)
            num >>= 4
            if num == 0: break
        def toH(x):
            if x < 10:
                return str(x)
            return chr(ord('a') + (x - 10))
        s = [toH(x) for x in s[::-1]]
        return ''.join(s)

so = Solution()
print(so.toHex(26))