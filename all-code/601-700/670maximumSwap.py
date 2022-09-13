# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
# 示例 1 :
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 示例 2 :
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
# 注意:
#
# 给定数字的范围是 [0, 108]





from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        s1 = str(num)
        s2 = ''.join(sorted(s1, reverse=True))
        n = len(s1)
        x, y = -1, -1
        for i in range(n):
            if s2[i] != s1[i]:
                x = i
                break
        if x == -1:
            return num
        y = s1.rfind(s2[i])
        ans = s1[:x] + s1[y] + s1[x + 1:y] + s1[x] + s1[y + 1:]
        return int(ans)



so = Solution()
# so.trimBST(root, 1, 2)


print(so.maximumSwap(2736))
print(so.maximumSwap(9973))

