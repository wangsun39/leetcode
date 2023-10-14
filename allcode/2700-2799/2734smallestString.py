# 给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以完成以下行为：
#
# 选则 s 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
# 返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。
#
# 子字符串 是字符串中的一个连续字符序列。
#
# 现有长度相同的两个字符串 x 和 字符串 y ，在满足 x[i] != y[i] 的第一个位置 i 上，如果  x[i] 在字母表中先于 y[i] 出现，则认为字符串 x 比字符串 y 字典序更小 。
#
#
# 示例 1：
#
# 输入：s = "cbabc"
# 输出："baabc"
# 解释：我们选择从下标 0 开始、到下标 1 结束的子字符串执行操作。
# 可以证明最终得到的字符串是字典序最小的。
# 示例 2：
#
# 输入：s = "acbbc"
# 输出："abaab"
# 解释：我们选择从下标 1 开始、到下标 4 结束的子字符串执行操作。
# 可以证明最终得到的字符串是字典序最小的。
# 示例 3：
#
# 输入：s = "leetcode"
# 输出："kddsbncd"
# 解释：我们选择整个字符串执行操作。
# 可以证明最终得到的字符串是字典序最小的。
#
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 仅由小写英文字母组成
from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        start = -1
        for i, x in enumerate(s):
            if x != 'a':
                start = i
                break
        if start == -1:
            return s[:n - 1] + 'z'
        pos = s.find('a', start)
        if pos == -1:
            end = n
        else:
            end = pos
        l = list(s)
        for i in range(start, end):
            if l[i] == 'a':
                l[i] = 'z'
            else:
                l[i] = chr(ord(l[i]) - 1)
        return ''.join(l)



so = Solution()
print(so.smallestString(s = "cbabc"))
print(so.smallestString(s = "acbbc"))
print(so.smallestString(s = "leetcode"))




