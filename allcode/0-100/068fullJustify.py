# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 示例 2:
#
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
# 示例 3:
#
# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getLine(wordsNum):
            numOfWords = len(wordsNum)
            isEnd = True
            if numOfWords <= 0:
                return 0, isEnd
            length = wordsNum[0]
            for i in range(1, numOfWords):
                length += (wordsNum[i] + 1)
                if length > maxWidth:
                    return i, False
            return numOfWords, isEnd
        def printLine(start, end):
            blank_num = maxWidth - sum(wordsNum[start:end])
            interval_num = end - start - 1
            a = blank_num // interval_num if interval_num > 0 else blank_num
            b = blank_num % interval_num if interval_num > 0 else 0
            res = ''
            for i in range(end - start):
                res += words[start + i]
                if i < end - start - 1 or 0 == interval_num:
                    if i < b:
                        res += (' ' * (a + 1))
                    else:
                        res += (' ' * a)
            return res
        def printLastLine(start, end):
            res = ''
            for i in range(end - start):
                res += words[start + i]
                if i < end - start - 1:
                    res += ' '
            length = len(res)
            res += (' ' * (maxWidth - length))
            return res

        i = 0
        res = []
        wordsNum = [len(i) for i in words]
        while True:
            numOfNextLine, isEnd = getLine(wordsNum[i:])
            if isEnd:
                line = printLastLine(i, i + numOfNextLine)
                res.append(line)
                break
            line = printLine(i, i+numOfNextLine)
            res.append(line)
            i += numOfNextLine
        return res



so = Solution()
print(so.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(so.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(so.fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20))


