# 给你一个字符串text，你需要使用 text 中的字母来拼凑尽可能多的单词"balloon"（气球）。
#
# 字符串text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词"balloon"。

#
# 示例 1：
#
#
#
# 输入：text = "nlaebolko"
# 输出：1
# 示例 2：
#
#
#
# 输入：text = "loonbalxballpoon"
# 输出：2
# 示例 3：
#
# 输入：text = "leetcode"
# 输出：0
#
#
# 提示：
#
# 1 <= text.length <= 10^4
# text全部由小写英文字母组成


from leetcode.allcode.competition.mypackage import *
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])



obj = Solution()
print(obj.maxNumberOfBalloons("loonbalxballpoon"))

