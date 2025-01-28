# 给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。
#
# 返回交换 任意 次之后 num 的 最大 可能值。
#
#
#
# 示例 1：
#
# 输入：num = 1234
# 输出：3412
# 解释：交换数字 3 和数字 1 ，结果得到 3214 。
# 交换数字 2 和数字 4 ，结果得到 3412 。
# 注意，可能存在其他交换序列，但是可以证明 3412 是最大可能值。
# 注意，不能交换数字 4 和数字 1 ，因为它们奇偶性不同。
# 示例 2：
#
# 输入：num = 65875
# 输出：87655
# 解释：交换数字 8 和数字 6 ，结果得到 85675 。
# 交换数字 5 和数字 7 ，结果得到 87655 。
# 注意，可能存在其他交换序列，但是可以证明 87655 是最大可能值。
#
#
# 提示：
#
# 1 <= num <= 109





from leetcode.allcode.competition.mypackage import *
class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        l = list(s)
        l = [int(i) for i in l]
        even, odds = [], []
        p1, p2 = [], []
        for i, e in enumerate(l):
            if l[i] % 2 == 0:
                even.append(e)
                p1.append(i)
            else:
                odds.append(e)
                p2.append(i)
        even.sort(reverse=True)
        odds.sort(reverse=True)
        i, j = 0, 0
        all = []
        while i < len(even) or j < len(odds):
            if j >= len(odds) or (i < len(even) and p1[i] < p2[j]):
                all.append(even[i])
                i += 1
            else:
                all.append(odds[j])
                j += 1
        # print(all)
        l = [str(i) for i in all]
        new = ''.join(l)
        # print(new)
        return int(new)

so = Solution()
# print(so.kthPalindrome([2,9,7,6], intLength = 1))
# print(so.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], intLength = 1))
# print(so.kthPalindrome([1,100,3,4,5,90], intLength = 3))
# print(so.kthPalindrome([1,2,3,4,5,90], intLength = 3))
# print(so.kthPalindrome([2,4,6], intLength = 4))

