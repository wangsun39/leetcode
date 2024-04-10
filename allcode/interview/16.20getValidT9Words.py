# 在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：
#
#
#
# 示例 1:
#
# 输入: num = "8733", words = ["tree", "used"]
# 输出: ["tree", "used"]
# 示例 2:
#
# 输入: num = "2", words = ["a", "b", "c", "d"]
# 输出: ["a", "b", "c"]
# 提示：
#
# num.length <= 1000
# words.length <= 500
# words[i].length == num.length
# num中不会出现 0, 1 这两个数字

from leetcode.allcode.competition.mypackage import *


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        d = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
        def toNum(word):
            res = [d[w] for w in word]
            return ''.join(res)
        ans = [word for word in words if toNum(word) == num]
        return ans





so = Solution()
print(so.getValidT9Words(num = "8733", words = ["tree", "used"]))
print(so.getValidT9Words(num = "2", words = ["a", "b", "c", "d"]))





