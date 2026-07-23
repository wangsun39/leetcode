# 给你一个字符串数组 words。
#
# 定义对字符串 s 的一次 变换 如下：
#
# 令 E 为 s 中位于偶数下标处字符组成的 子序列。
# 令 O 为 s 中位于奇数下标处字符组成的 子序列。
# 分别将 E 和 O 向右循环移动 任意 个位置，移动次数可以为 0。
# 将移动后的 E 中的字符依次放回偶数下标，将移动后的 O 中的字符依次放回奇数下标，从而重新构造字符串。
# 如果一个字符串可以通过 一次 变换得到另一个字符串，则称这两个字符串 等价 。
#
# 将 words 划分为 最少 数量的组，并满足：
#
# 每个字符串 恰好 属于一个组。
# 同一组中的任意两个字符串都 等价。
# 返回一个整数，表示所需的 最少 分组数量。
#
# 子序列 是指通过删除一个序列中的某些元素或不删除任何元素，并且不改变剩余元素相对顺序后得到的序列。
#
#
#
# 示例 1：
#
# 输入： words = ["ntgwz","zwntg"]
#
# 输出： 1
#
# 解释：
#
# 对于 "ntgwz"，偶数下标字符组成的子序列为 "ngz"，奇数下标字符组成的子序列为 "tw"。
# 将 "ngz" 向右循环移动 1 位，得到 "zng"；将 "tw" 向右循环移动 1 位，得到 "wt"。
# 重新构造字符串后，得到 "zwntg"。
# 因此，这两个字符串等价，可以划分到同一组中。
# 示例 2：
#
# 输入： words = ["abc","cab","bac","acb","bca","cba"]
#
# 输出： 3
#
# 解释：
#
# 这些字符串可以划分为以下各组：
#
# ["abc","cba"]
# ["cab","bac"]
# ["acb","bca"]
# 示例 3：
#
# 输入： words = ["leet","abb","bab","deed","edde","code","bba"]
#
# 输出： 5
#
# 解释：
#
# 这些字符串可以划分为以下各组：
#
# ["abb","bba"]
# ["deed","edde"]
# ["leet"]
# ["bab"]
# ["code"]
# 每组中的任意两个字符串都等价。
#
#
#
# 提示：
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 5 * 105
# 所有 words[i].length 之和不超过 5 * 105。
# words[i] 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        s = set()
        for word in words:
            m = len(word)
            e = [word[i] for i in range(0, m, 2)]
            mn_e = 0
            o = [word[i] for i in range(1, m, 2)]
            mn_o = 0
            ne, no = len(e), len(o)
            i = 1
            while i < ne:
                j = 0
                while j < ne and e[(mn_e + j) % ne] == e[(i + j) % ne]:
                    j += 1
                if j == ne or e[(mn_e + j) % ne] < e[(i + j) % ne]:
                    i += j + 1  # 关键跳跃步骤
                else:
                    mn_e = i
                    i += 1
            i = 1
            while i < no:
                j = 0
                while j < no and o[(mn_o + j) % no] == o[(i + j) % no]:
                    j += 1
                if j == no or o[(mn_o + j) % no] < o[(i + j) % no]:
                    i += j + 1  # 关键跳跃步骤
                else:
                    mn_o = i
                    i += 1
            e1, o1 = ''.join(e[mn_e:] + e[: mn_e]), ''.join(o[mn_o:] + o[: mn_o])
            s.add(e1 + o1)

        return len(s)



so = Solution()
print(so.minimumGroups(words = ["ntgwz","zwntg"]))



