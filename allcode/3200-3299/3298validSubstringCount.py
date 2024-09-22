# 给你两个字符串 word1 和 word2 。
#
# 如果一个字符串 x 重新排列后，word2 是重排字符串的
# 前缀
#  ，那么我们称字符串 x 是 合法的 。
#
# 请你返回 word1 中 合法
# 子字符串
#  的数目。
#
# 注意 ，这个问题中的内存限制比其他题目要 小 ，所以你 必须 实现一个线性复杂度的解法。
#
#
#
# 示例 1：
#
# 输入：word1 = "bcca", word2 = "abc"
#
# 输出：1
#
# 解释：
#
# 唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。
#
# 示例 2：
#
# 输入：word1 = "abcabc", word2 = "abc"
#
# 输出：10
#
# 解释：
#
# 除了长度为 1 和 2 的所有子字符串都是合法的。
#
# 示例 3：
#
# 输入：word1 = "abcabc", word2 = "aaabc"
#
# 输出：0
#
#
#
# 解释：
#
# 1 <= word1.length <= 106
# 1 <= word2.length <= 104
# word1 和 word2 都只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        c2 = Counter(word2)
        target = [0] * 26
        for k, v in c2.items():
            target[c2i[k]] = v
        source = [0] * 26
        ns = set(i for i, x in enumerate(target) if x > 0)  # 不等的集合
        def check():
            return len(ns) == 0
        n = len(word1)
        r = 0
        ans = 0
        for l in range(n):
            if l > 0:
                pre = c2i[word1[l - 1]]
                source[pre] -= 1
                if source[pre] < target[pre]:
                    ns.add(pre)
            while r < n:
                if check():
                    break
                y = c2i[word1[r]]
                source[y] += 1
                if source[y] >= target[y] and y in ns:
                    ns.remove(y)
                r += 1
            if check():
                ans += n - r + 1

        return ans


so = Solution()
print(so.validSubstringCount(word1 = "bbbbbbbbbbbbbbb", word2 = "bb"))
print(so.validSubstringCount(word1 = "abcabc", word2 = "abc"))
print(so.validSubstringCount(word1 = "bcca", word2 = "abc"))
print(so.validSubstringCount(word1 = "abcabc", word2 = "aaabc"))




