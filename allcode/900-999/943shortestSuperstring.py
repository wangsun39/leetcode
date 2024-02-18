# 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。
#
# 我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。
#
#
#
# 示例 1：
#
# 输入：words = ["alex","loves","leetcode"]
# 输出："alexlovesleetcode"
# 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
# 示例 2：
#
# 输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# 输出："gctaagttcatgcatc"
#
#
# 提示：
#
# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] 由小写英文字母组成
# words 中的所有字符串 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        words.append('')  # 增加一个空串，方便后面从空串出发进行DFS
        n = len(words)
        w = [[0] * n for _ in range(n)]  # w[i][j]  表示word[i]之后拼接 word[j] 扩展出来的最小长度
        def calc(w1, w2):
            n1, n2 = len(w1), len(w2)
            for i in range(1, n1):
                if w2.startswith(w1[i:]):
                    return n2 - (n1 - i)
            return n2
        for i in range(n):
            for j in range(n):
                if i != j:
                    w[i][j] = calc(words[i], words[j])

        @cache
        def dfs(idx, vis):
            if vis == (1 << n) - 1:
                return 0, ''
            mn, res = inf, ''
            for i in range(n):
                if (1 << i) & vis == 0:
                    l, s = dfs(i, vis | (1 << i))
                    lw = w[idx][i]
                    l += lw
                    if mn > l:
                        mn = l
                        res = words[i][-lw:] + s
            return mn, res
        return dfs(n - 1, 0)[1]




so = Solution()
print(so.shortestSuperstring(words = ["alex","loves","leetcode"]))
print(so.shortestSuperstring(words = ["catg","ctaagt","gcta","ttca","atgcatc"]))




