# 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
#
#
# 示例 1：
#
# 输入：s = "Hello World"
# 输出：5
# 示例 2：
#
# 输入：s = " "
# 输出：0
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成



from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        start, end = -1, -1
        for i in range(N - 1, -1, -1):
            if -1 == end and ' ' != s[i]:
                end = i
            elif -1 != end and ' ' == s[i]:
                start = i
                break
        print(start, end)
        return end - start


so = Solution()
print(so.lengthOfLastWord("Hello World"))
print(so.lengthOfLastWord("Hello World "))
print(so.lengthOfLastWord(" "))
print(so.lengthOfLastWord(""))
