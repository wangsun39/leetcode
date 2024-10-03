from leetcode.allcode.competition.mypackage import *


# 给定一个整数，打印该整数的英文描述。
#
# 示例 1:
#
# 输入: 123
# 输出: "One Hundred Twenty Three"
# 示例 2:
#
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
# 示例 3:
#
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 示例 4:
#
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# 注意：本题与 273 题相同：https://leetcode-cn.com/problems/integer-to-english-words/


class Solution:
    def numberToWords(self, num: int) -> str:
        one = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teen = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        ty = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        def less1000(x):
            res = []
            if x >= 100:
                res.append(one[x // 100] + ' Hundred')
                x %= 100
            if x >= 20:
                res.append(ty[x // 10])
                x %= 10
            elif x >= 10:
                res.append(teen[x - 10])
                x %= 10
                return ' '.join(res)
            if x > 0:
                res.append(one[x])
            return ' '.join(res)
        ans = []
        if num >= 1000 * 1000 * 1000:
            ans.append(one[num // (1000 * 1000 * 1000)] + ' Billion')
            num %= (1000 * 1000 * 1000)
        if num >= 1000 * 1000:
            ans.append(less1000(num // (1000 * 1000)) + ' Million')
            num %= (1000 * 1000)
        if num >= 1000:
            ans.append(less1000(num // 1000) + ' Thousand')
            num %= 1000
        if num > 0:
            ans.append(less1000(num))
        if num == 0:
            ans.append(one[num])
        return ' '.join(ans)






so = Solution()
print(so.numberToWords(12345))
print(so.numberToWords(123))
print(so.numberToWords(3))
print(so.numberToWords(1234567))
print(so.numberToWords(1234567891))





