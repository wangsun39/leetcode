# 你想要用小写字母组成一个目标字符串target。
#
# 开始的时候，序列由target.length个'?'记号组成。而你有一个小写字母印章stamp。
#
# 在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行10 * target.length 个回合。
#
# 举个例子，如果初始序列为 "?????"，而你的印章 stamp是"abc"，那么在第一回合，你可以得到"abc??"、"?abc?"、"??abc"。（请注意，印章必须完全包含在序列的边界内才能盖下去。）
#
# 如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。
#
# 例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作"?????" -> "abc??" -> "ababc" 相对应的答案 [0, 2]；
#
# 另外，如果可以印出序列，那么需要保证可以在 10 * target.length个回合内完成。任何超过此数字的答案将不被接受。
#
#
#
# 示例 1：
#
# 输入：stamp = "abc", target = "ababc"
# 输出：[0,2]
# （[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
# 示例 2：
#
# 输入：stamp = "abca", target = "aabcaca"
# 输出：[3,0,1]
#
#
# 提示：
#
# 1 <= stamp.length <= target.length <= 1000
# stamp 和target只包含小写字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        n, m = len(target), len(stamp)
        vis = [0] * (n - m + 1)
        def equal(idx):
            return all(target[idx + i] == '?' or target[idx + i] == stamp[i] for i in range(m))
        ans = []
        for _ in range(n - m + 1):  # 至多进行的次数
            chg = False
            for i in range(n - m + 1):
                if not vis[i] and equal(i):
                    for j in range(m):
                        target[i + j] = '?'
                    vis[i] = 1
                    chg = True
                    ans.insert(0, i)
                    break
            if not chg: return []
            if all(x == '?' for x in target):
                break
        return ans

so = Solution()
print(so.movesToStamp(stamp = "abc", target = "ababc"))
print(so.movesToStamp(stamp = "abca", target = "aabcaca"))




