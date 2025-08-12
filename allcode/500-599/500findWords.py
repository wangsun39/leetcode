# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#
# 请注意，字符串 不区分大小写，相同字母的大小写形式都被视为在同一行。
#
# 美式键盘 中：
#
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
# American keyboard
#
#
#
# 示例 1：
#
# 输入：words = ["Hello","Alaska","Dad","Peace"]
#
# 输出：["Alaska","Dad"]
#
# 解释：
#
# 由于不区分大小写，"a" 和 "A" 都在美式键盘的第二行。
#
# 示例 2：
#
# 输入：words = ["omk"]
#
# 输出：[]
#
# 示例 3：
#
# 输入：words = ["adsdf","sfd"]
#
# 输出：["adsdf","sfd"]
#
#
#
# 提示：
#
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] 由英文字母（小写和大写字母）组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        for x in 'qwertyuiopQWERTYUIOP':
            d[x] = 1
        for x in 'asdfghjklASDFGHJKL':
            d[x] = 2
        for x in 'zxcvbnmZXCVBNM':
            d[x] = 3
        ans = []
        for w in words:
            if all(d[x] == d[w[0]] for x in w):
                ans.append(w)
        return ans


so = Solution()
print(so.findWords(words = ["Hello","Alaska","Dad","Peace"]))

