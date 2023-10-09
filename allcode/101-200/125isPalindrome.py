# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false



from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        if N <= 1:
            return True
        i, j = 0, N - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            # if s[i].isdigit() or s[j].isdigit():
            #     if s[i] == s[j]:
            #         i += 1
            #         j -= 1
            #         continue
            #     else:
            #         return False
            if s[i].upper() == s[j].upper():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True


so = Solution()

print(so.isPalindrome("A man, a plan, a canal: Panama"))
print(so.isPalindrome("race a car"))

