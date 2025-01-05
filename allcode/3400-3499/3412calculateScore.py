# 给你一个字符串 s。
#
# 英文字母中每个字母的 镜像 定义为反转字母表之后对应位置上的字母。例如，'a' 的镜像是 'z'，'y' 的镜像是 'b'。
#
# 最初，字符串 s 中的所有字符都 未标记 。
#
# 字符串 s 的初始分数为 0 ，你需要对其执行以下过程：
#
# 从左到右遍历字符串。
# 对于每个下标 i ，找到距离最近的 未标记 下标 j，下标 j 需要满足 j < i 且 s[j] 是 s[i] 的镜像。然后 标记 下标 i 和 j，总分加上 i - j 的值。
# 如果对于下标 i，不存在满足条件的下标 j，则跳过该下标，继续处理下一个下标，不需要进行标记。
# 返回最终的总分。
#
#
#
# 示例 1：
#
# 输入： s = "aczzx"
#
# 输出： 5
#
# 解释：
#
# i = 0。没有符合条件的下标 j，跳过。
# i = 1。没有符合条件的下标 j，跳过。
# i = 2。距离最近的符合条件的下标是 j = 0，因此标记下标 0 和 2，然后将总分加上 2 - 0 = 2 。
# i = 3。没有符合条件的下标 j，跳过。
# i = 4。距离最近的符合条件的下标是 j = 1，因此标记下标 1 和 4，然后将总分加上 4 - 1 = 3 。
# 示例 2：
#
# 输入： s = "abcdef"
#
# 输出： 0
#
# 解释：
#
# 对于每个下标 i，都不存在满足条件的下标 j。
#
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def calculateScore(self, s: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = [c2i[x] for x in s]
        d = defaultdict(list)
        ans = 0
        for i, x in enumerate(s):
            if len(d[25 - x]) == 0:
                d[x].append(i)
            else:
                j = d[25 - x].pop()
                ans += (i - j)
        return ans


so = Solution()
print(so.calculateScore(s = "aczzx"))




