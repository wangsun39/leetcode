# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
#
#
#
# 示例 1：
#
# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
# 示例 2：
#
# 输入：s = "leetcodeisgreat"
# 输出：5
# 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
# 示例 3：
#
# 输入：s = "bcbcbc"
# 输出：6
# 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
#
#
# 提示：
#
# 1 <= s.length <= 5 x 10^5
# s 只包含小写英文字母。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0: -1}  # k: v  表示出现k的最小下标，k表示五个元音的奇偶性
        cur = 0  # 按位，0: 表示奇数，1: 表示偶数
        ans = 0
        for i, x in enumerate(s):
            if x == 'a':
                cur ^= (1 << 0)
            elif x == 'e':
                cur ^= (1 << 1)
            elif x == 'i':
                cur ^= (1 << 2)
            elif x == 'o':
                cur ^= (1 << 3)
            elif x == 'u':
                cur ^= (1 << 4)
            if cur not in d:
                d[cur] = i
            else:
                ans = max(ans, i - d[cur])
        return ans



so = Solution()
print(so.findTheLongestSubstring("eleetminicoworoep"))
print(so.findTheLongestSubstring("leetcodeisgreat"))
print(so.findTheLongestSubstring("bcbcbc"))





