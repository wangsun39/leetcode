# 给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。
#
# 对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
#
#
#
# 示例 1：
#
# 输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
# 输出：["girl","student"]
# 示例 2：
#
# 输入：text = "we will we will rock you", first = "we", second = "will"
# 输出：["we","rock"]
#
#
# 提示：
#
# 1 <= text.length <= 1000
# text 由小写英文字母和空格组成
# text 中的所有单词之间都由 单个空格字符 分隔
# 1 <= first.length, second.length <= 10
# first 和 second 由小写英文字母组成
# text 不包含任何前缀或尾随空格。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        cnt = 0
        ans = []
        for x in text:
            if cnt == 1:
                if x == second:
                    cnt = 2
                    continue
            elif cnt == 2:
                ans.append(x)
                if first == second == x:
                    cnt = 2
                    continue

            if x == first:
                cnt = 1
                continue
            cnt = 0
        return ans

so = Solution()
print(so.findOcurrences(text = "we we we we will rock you", first = "we", second = "we"))
print(so.findOcurrences(text = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa", first = "kcyxdfnoa", second = "jkypmsxd"))
print(so.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))

