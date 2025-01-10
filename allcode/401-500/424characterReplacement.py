# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
#
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
#
#
#
# 示例 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 示例 2：
#
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由大写英文字母组成
# 0 <= k <= s.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        def calc(ch):
            dq = deque()
            pre = -1
            other = 0
            res = 0
            for i, x in enumerate(s):
                if pre == -1:
                    if x == ch:
                        pre = x
                    continue
                if x != ch:
                    other += 1
                    if other > k:
                        if dq:
                            pre = dq.popleft()
                        else:
                            pre = -1
                if x == ch:
                    dq.append(i)
                    res = max(res, i - pre + 1)





so = Solution()
print(so.characterReplacement([3,10,5,25,2,8]))


