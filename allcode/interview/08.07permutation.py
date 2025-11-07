# 无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
#
# 示例 1：
#
#  输入：S = "qwe"
#  输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
# 示例 2：
#
#  输入：S = "ab"
#  输出：["ab", "ba"]
# 提示：
#
# 字符都是英文字母。
# 字符串长度在[1, 9]之间。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = list(permutations(S))
        return [''.join(x) for x in ans]



so = Solution()



