# 给你一个字符串 word 和一个 非负 整数 k。
#
# 返回 word 的
# 子字符串
#  中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。
#
#
#
# 示例 1：
#
# 输入：word = "aeioqq", k = 1
#
# 输出：0
#
# 解释：
#
# 不存在包含所有元音字母的子字符串。
#
# 示例 2：
#
# 输入：word = "aeiou", k = 0
#
# 输出：1
#
# 解释：
#
# 唯一一个包含所有元音字母且不含辅音字母的子字符串是 word[0..4]，即 "aeiou"。
#
# 示例 3：
#
# 输入：word = "ieaouqqieaouqq", k = 1
#
# 输出：3
#
# 解释：
#
# 包含所有元音字母并且恰好含有一个辅音字母的子字符串有：
#
# word[0..5]，即 "ieaouq"。
# word[6..11]，即 "qieaou"。
# word[7..12]，即 "ieaouq"。
#
#
# 提示：
#
# 5 <= word.length <= 250
# word 仅由小写英文字母组成。
# 0 <= k <= word.length - 5

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        d = defaultdict(int)
        cnt = 0  # 当前窗口内元音字母个数
        n = len(word)
        r = 0
        ans = 0
        right = [n] * n  # 记录i右侧第一个辅音的位置
        cur = n
        for i in range(n - 1, -1, -1):
            right[i] = cur
            if word[i] not in 'aeiou':
                cur = i
        for l in range(n):
            x = word[l]
            while r < n:
                if r - l - cnt > k:
                    break
                if len(d) == 5 and r - l - cnt == k:
                    ans += (right[r - 1] - (r - 1))
                    break
                y = word[r]
                if y in 'aeiou':
                    d[y] += 1
                    cnt += 1
                r += 1
            if r == n and len(d) == 5 and r - l - cnt == k:
                ans += 1
            if x in 'aeiou':
                d[x] -= 1
                if d[word[l]] == 0:
                    del (d[word[l]])
                cnt -= 1
        return ans


so = Solution()
print(so.countOfSubstrings(word = "ouiaoe", k = 0))  # 2
print(so.countOfSubstrings(word = "iqeaouqi", k = 2))  # 3
print(so.countOfSubstrings(word = "aeiou", k = 0))  # 1
print(so.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))  # 3
print(so.countOfSubstrings(word = "aeioqq", k = 1))  # 0




