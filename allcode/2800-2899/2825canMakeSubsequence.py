# 给你一个下标从 0 开始的字符串 str1 和 str2 。
#
# 一次操作中，你选择 str1 中的若干下标。对于选中的每一个下标 i ，你将 str1[i] 循环 递增，变成下一个字符。也就是说 'a' 变成 'b' ，'b' 变成 'c' ，以此类推，'z' 变成 'a' 。
#
# 如果执行以上操作 至多一次 ，可以让 str2 成为 str1 的子序列，请你返回 true ，否则返回 false 。
#
# 注意：一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。
#
#
#
# 示例 1：
#
# 输入：str1 = "abc", str2 = "ad"
# 输出：true
# 解释：选择 str1 中的下标 2 。
# 将 str1[2] 循环递增，得到 'd' 。
# 因此，str1 变成 "abd" 且 str2 现在是一个子序列。所以返回 true 。
# 示例 2：
#
# 输入：str1 = "zc", str2 = "ad"
# 输出：true
# 解释：选择 str1 中的下标 0 和 1 。
# 将 str1[0] 循环递增得到 'a' 。
# 将 str1[1] 循环递增得到 'd' 。
# 因此，str1 变成 "ad" 且 str2 现在是一个子序列。所以返回 true 。
# 示例 3：
#
# 输入：str1 = "ab", str2 = "d"
# 输出：false
# 解释：这个例子中，没法在执行一次操作的前提下，将 str2 变为 str1 的子序列。
# 所以返回 false 。
#
#
# 提示：
#
# 1 <= str1.length <= 105
# 1 <= str2.length <= 105
# str1 和 str2 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        j = 0
        for i in range(n2):
            found = False
            while j < n1:
                if str1[j] == str2[i]:
                    j += 1
                    found = True
                    break
                if str2[i] == 'a' and str1[j] == 'z':
                    j += 1
                    found = True
                    break
                if ord(str2[i]) == ord(str1[j]) + 1:
                    j += 1
                    found = True
                    break
                j += 1
            if not found:
                return False
        return True




so = Solution()
print(so.canMakeSubsequence("ffbczn", "gba"))
print(so.canMakeSubsequence(str1 = "zc", str2 = "ad"))
print(so.canMakeSubsequence(str1 = "abc", str2 = "ad"))
print(so.canMakeSubsequence(str1 = "ab", str2 = "d"))




