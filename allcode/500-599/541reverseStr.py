# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔2k 个字符的前 k 个字符进行反转。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
#
# 示例:
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
# 提示：
#
# 该字符串只包含小写英文字母。
# 给定字符串的长度和 k 在 [1, 10000] 范围内。


from typing import List
from collections import defaultdict

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count, stack = 0, []
        res = ''
        for i in s:
            count += 1
            if count <= k:
                stack.append(i)
                if count == k:
                    while len(stack) > 0:
                        res += stack.pop()
            else:
                res += i
                if count == k * 2:
                    count = 0
        while len(stack) > 0:
            res += stack.pop()
        return res


so = Solution()
print(so.reverseStr(s = "abcdefg", k = 2))
print(so.reverseStr(s = "abcde", k = 2))

