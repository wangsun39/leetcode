# 将非负整数 num 转换为其对应的英文表示。
#
#  
#
# 示例 1：
#
# 输入：num = 123
# 输出："One Hundred Twenty Three"
# 示例 2：
#
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
# 示例 3：
#
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 示例 4：
#
# 输入：num = 1234567891
# 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
#  
#
# 提示：
#
# 0 <= num <= 231 - 1




class Solution:
    def numberToWords(self, num: int) -> str:
        i2s1 = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        i2s2 = {0: '', 1: '', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        i2s3 = {0: 'Ten', 1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}
        def lessThan1000(num):
            hundreds = num // 100
            tens = (num - hundreds * 100) // 10
            ones = num % 10
            res = '' if 0 == hundreds else ' ' + i2s1[hundreds] + ' Hundred'
            if 1 == tens:
                res += (' ' + i2s3[ones])
                return res
            if tens > 1:
                res += (' ' + i2s2[tens])
            res += (' ' + i2s1[ones]) if ones > 0 else ''
            return res
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        res = ''
        if billion > 0:
            res += (lessThan1000(billion) + ' Billion')
        if million > 0:
            res += ('' + lessThan1000(million) + ' Million')
        if thousand > 0:
            res += ('' + lessThan1000(thousand) + ' Thousand')
        res += ('' + lessThan1000(num % 1000))
        res = res.strip()
        return res if 0 != len(res) else 'Zero'


so = Solution()
print(so.numberToWords(50868))
print(so.numberToWords(1001))
print(so.numberToWords(0))
print(so.numberToWords(12345))
print(so.numberToWords(123))
print(so.numberToWords(1234567))
print(so.numberToWords(1234567891))

