# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#
#
# 示例：
#
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#
#
# 提示：
#
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。



from leetcode.allcode.competition.mypackage import *


class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split(' ')
        s1 = [e[::-1] for e in s1]
        return ' '.join(s1)


so = Solution()
print(so.reverseWords("Let's take LeetCode contest"))

