# 给你一个字符串 s 。
#
# 如果字符串 t 中的字符出现次数相等，那么我们称 t 为 好的 。
#
# 你可以执行以下操作 任意次 ：
#
# 从 s 中删除一个字符。
# 往 s 中添加一个字符。
# 将 s 中一个字母变成字母表中下一个字母。
# 注意 ，第三个操作不能将 'z' 变为 'a' 。
#
# 请你返回将 s 变 好 的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：s = "acab"
#
# 输出：1
#
# 解释：
#
# 删掉一个字符 'a' ，s 变为好的。
#
# 示例 2：
#
# 输入：s = "wddw"
#
# 输出：0
#
# 解释：
#
# s 一开始就是好的，所以不需要执行任何操作。
#
# 示例 3：
#
# 输入：s = "aaabc"
#
# 输出：2
#
# 解释：
#
# 通过以下操作，将 s 变好：
#
# 将一个 'a' 变为 'b' 。
# 往 s 中插入一个 'c' 。
#
#
# 提示：
#
# 1 <= s.length <= 2 * 104
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def makeStringGood(self, s: str) -> int:
        counter = [0] * 26
        for x in s:
            counter[ord(x) - ord('a')] += 1

        ans = inf
        mx_cnt = max(counter)
        for cnt in range(mx_cnt + 1):
            # 枚举最终相等的数量
            dp = [inf] * 27  # 从 i 开始向后，达到数量都是 cnt 的最小操作次数
            dp[-1] = 0
            dp[25] = MIN(counter[-1], abs(cnt - counter[-1]))
            for j in range(24, -1, -1):
                dp[j] = MIN(counter[j], abs(cnt - counter[j])) + dp[j + 1]  # 单独处理 j

                # 下面是组合处理 j 和 j + 1
                if counter[j + 1] >= cnt:  # 不能从i变成j
                    continue
                if counter[j] > cnt:
                    if counter[j] - cnt > cnt - counter[j + 1]:
                        dp[j] = MIN(dp[j], counter[j] - cnt + dp[j + 2])
                    else:
                        dp[j] = MIN(dp[j], cnt - counter[j + 1] + dp[j + 2])
                else:
                    if counter[j] > cnt - counter[j + 1]:
                        dp[j] = MIN(dp[j], counter[j] + dp[j + 2])
                    else:
                        dp[j] = MIN(dp[j], cnt - counter[j + 1] + dp[j + 2])
            ans = MIN(ans, dp[0])
        return ans




so = Solution()
print(so.makeStringGood("gigigjjggjjgg"))




