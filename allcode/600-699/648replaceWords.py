# 在英语中，我们有一个叫做词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。例如，词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。
#
# 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
#
# 你需要输出替换之后的句子。
#
#
#
# 示例 1：
#
# 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# 输出："the cat was rat by the bat"
# 示例 2：
#
# 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# 输出："a a b c"
#
#
# 提示：
#
# 1 <= dictionary.length<= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i]仅由小写字母组成。
# 1 <= sentence.length <= 10^6
# sentence仅由小写字母和空格组成。
# sentence 中单词的总量在范围 [1, 1000] 内。
# sentence 中每个单词的长度在范围 [1, 1000] 内。
# sentence 中单词之间由一个空格隔开。
# sentence没有前导或尾随空格。


# Definition for a binary tree node.
from leetcode.allcode.competition.mypackage import *

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set(dictionary)
        def trans(word):
            n = len(word)
            for i in range(1, n + 1):
                if word[:i] in s:
                    return word[:i]
            return word
        words = sentence.split(' ')
        res = []
        for word in words:
            res.append(trans(word))
        return ' '.join(res)



so = Solution()


