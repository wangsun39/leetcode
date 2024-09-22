# 给你一个字符串数组 message 和一个字符串数组 bannedWords。
#
# 如果数组中 至少 存在两个单词与 bannedWords 中的任一单词 完全相同，则该数组被视为 垃圾信息。
#
# 如果数组 message 是垃圾信息，则返回 true；否则返回 false。
#
#
#
# 示例 1：
#
# 输入： message = ["hello","world","leetcode"], bannedWords = ["world","hello"]
#
# 输出： true
#
# 解释：
#
# 数组 message 中的 "hello" 和 "world" 都出现在数组 bannedWords 中。
#
# 示例 2：
#
# 输入： message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]
#
# 输出： false
#
# 解释：
#
# 数组 message 中只有一个单词（"programming"）出现在数组 bannedWords 中。
#
#
#
# 提示：
#
# 1 <= message.length, bannedWords.length <= 105
# 1 <= message[i].length, bannedWords[i].length <= 15
# message[i] 和 bannedWords[i] 都只由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        cnt = sum(1 for x in message if x in bannedWords)
        return cnt > 1


so = Solution()
print(so.reportSpam(message = ["hello","world","leetcode"], bannedWords = ["world","hello"]))
print(so.reportSpam(message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]))




