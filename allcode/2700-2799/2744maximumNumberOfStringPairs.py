# 给你一个下标从 0 开始的数组 words ，数组中包含 互不相同 的字符串。
#
# 如果字符串 words[i] 与字符串 words[j] 满足以下条件，我们称它们可以匹配：
#
# 字符串 words[i] 等于 words[j] 的反转字符串。
# 0 <= i < j < words.length
# 请你返回数组 words 中的 最大 匹配数目。
#
# 注意，每个字符串最多匹配一次。
#
#
#
# 示例 1：
#
# 输入：words = ["cd","ac","dc","ca","zz"]
# 输出：2
# 解释：在此示例中，我们可以通过以下方式匹配 2 对字符串：
# - 我们将第 0 个字符串与第 2 个字符串匹配，因为 word[0] 的反转字符串是 "dc" 并且等于 words[2]。
# - 我们将第 1 个字符串与第 3 个字符串匹配，因为 word[1] 的反转字符串是 "ca" 并且等于 words[3]。
# 可以证明最多匹配数目是 2 。
# 示例 2：
#
# 输入：words = ["ab","ba","cc"]
# 输出：1
# 解释：在此示例中，我们可以通过以下方式匹配 1 对字符串：
# - 我们将第 0 个字符串与第 1 个字符串匹配，因为 words[1] 的反转字符串 "ab" 与 words[0] 相等。
# 可以证明最多匹配数目是 1 。
# 示例 3：
#
# 输入：words = ["aa","ab"]
# 输出：0
# 解释：这个例子中，无法匹配任何字符串。
#
#
# 提示：
#
# 1 <= words.length <= 50
# words[i].length == 2
# words 包含的字符串互不相同。
# words[i] 只包含小写英文字母。

# 给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：
#
# 一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，开销为 cost[i] 单位的钱。
# 一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
# 请你返回刷完 n 堵墙最少开销为多少。
#
#
#
# 示例 1：
#
# 输入：cost = [1,2,3,2], time = [1,2,3,2]
# 输出：3
# 解释：下标为 0 和 1 的墙由付费油漆匠来刷，需要 3 单位时间。同时，免费油漆匠刷下标为 2 和 3 的墙，需要 2 单位时间，开销为 0 。总开销为 1 + 2 = 3 。
# 示例 2：
#
# 输入：cost = [2,3,4,2], time = [1,1,1,1]
# 输出：4
# 解释：下标为 0 和 3 的墙由付费油漆匠来刷，需要 2 单位时间。同时，免费油漆匠刷下标为 1 和 2 的墙，需要 2 单位时间，开销为 0 。总开销为 2 + 2 = 4 。
#
#
# 提示：
#
# 1 <= cost.length <= 500
# cost.length == time.length
# 1 <= cost[i] <= 106
# 1 <= time[i] <= 500

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        ans = 0
        for word in words:
            if word[::-1] in s and word != word[::-1]:
                ans += 1
        return ans // 2

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # 2024/1/17 另一种写法
        s = set()
        ans = 0
        for x in words:
            y = x[::-1]
            if y in s:
                s.remove(y)
                ans += 1
            else:
                s.add(x)
        return ans




so = Solution()
print(so.maximumNumberOfStringPairs(["ff","tx","qr","zw","wr","jr","zt","jk","sq","xx"]))
print(so.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
print(so.maximumNumberOfStringPairs(words = ["ab","ba","cc"]))
print(so.maximumNumberOfStringPairs(["aa","ab"]))




