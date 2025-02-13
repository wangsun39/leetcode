# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
#
#
# 示例 1：
#
# 输入："hello"
# 输出："holle"
# 示例 2：
#
# 输入："leetcode"
# 输出："leotcede"
#
#
# 提示：
#
# 元音字母不包含字母 "y" 。


from typing import List
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        N = len(s)
        i, j = 0, N - 1
        while i < j:
            if s[i] in 'aeiouAEIOU':
                if s[j] in 'aeiouAEIOU':
                    s[i], s[j] = s[j], s[i]
                    i += 1
                j -= 1
            else:
                i += 1
        return ''.join(s)


so = Solution()

print(so.reverseVowels("hello"))
print(so.reverseVowels("leetcode"))




