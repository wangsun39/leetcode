# 你有一个单词列表words和一个模式pattern，你想知道 words 中的哪些单词与模式匹配。
#
# 如果存在字母的排列 p，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
#
# （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
#
# 返回 words 中与给定模式匹配的单词列表。
#
# 你可以按任何顺序返回答案。
#
#
#
# 示例：
#
# 输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# 输出：["mee","aqq"]
# 解释：
# "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
# "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
# 因为 a 和 b 映射到同一个字母。
#
#
# 提示：
#
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length<= 20


from leetcode.allcode.competition.mypackage import *

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def suit(word):
            d = {}
            s = set()
            if len(word) != len(pattern):
                return False
            n = len(word)
            for i in range(n):
                if word[i] in d:
                    if d[word[i]] != pattern[i]:
                        return False
                else:
                    if pattern[i] in s:
                        return False
                    d[word[i]] = pattern[i]
                    s.add(pattern[i])
            return True
        ans = []
        for word in words:
            if suit(word):
                ans.append(word)
        return ans


so = Solution()
print(so.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))

