# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。
#
#
# 示例 1：
#
# 输入：words = ["bella","label","roller"]
# 输出：["e","l","l"]
# 示例 2：
#
# 输入：words = ["cool","lock","cook"]
# 输出：["c","o"]
#
#
# 提示：
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 由小写英文字母组成


from leetcode.allcode.competition.mypackage import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for w in words[1:]:
            c &= Counter(w)
        ans = []
        for k, v in c.items():
            ans += [k] * v
        return ans





obj = Solution()

