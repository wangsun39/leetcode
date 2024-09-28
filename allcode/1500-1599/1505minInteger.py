# 给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。
#
# 你可以交换这个整数相邻数位的数字 最多 k 次。
#
# 请你返回你能得到的最小整数，并以字符串形式返回。
#
#
#
# 示例 1：
#
#
#
# 输入：num = "4321", k = 4
# 输出："1342"
# 解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。
# 示例 2：
#
# 输入：num = "100", k = 1
# 输出："010"
# 解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。
# 示例 3：
#
# 输入：num = "36789", k = 1000
# 输出："36789"
# 解释：不需要做任何交换。
# 示例 4：
#
# 输入：num = "22", k = 22
# 输出："22"
# 示例 5：
#
# 输入：num = "9438957234785635408", k = 23
# 输出："0345989723478563548"
#
#
# 提示：
#
# 1 <= num.length <= 30000
# num 只包含 数字 且不含有 前导 0 。
# 1 <= k <= 10^9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        pos = defaultdict(list)  # pos[i]  记录每个字符i的位置
        for i, x in enumerate(num):
            pos[int(x)].append(i)
        idx = [0] * 10  # 记录剩余的字符的下标
        rmv = SortedList()  # 记录已经移到前面的数字的下标的有序列表
        n = len(num)
        ans = []
        for i in range(n):
            x = num[i]
            for j in range(10):
                if idx[j] == len(pos[j]): continue
                # 尝试把原来在 pos[j][idx[j]] 位置的 j 移到 位置 i，需要多少次交换
                p1 = rmv.bisect_left(pos[j][idx[j]])
                p2 = len(rmv) - p1  # 在删除列表中有p2个元素在 当前j 右侧，表示 当前j 已经右移了p2个位置
                dis = pos[j][idx[j]] + p2 - i  # 当前j 移动到位置i的交换次数
                if dis > k: continue
                k -= dis
                rmv.add(pos[j][idx[j]])
                idx[j] += 1
                ans.append(str(j))
                break
            if len(ans) < i + 1:
                ans.append(x)
        return ''.join(ans)


so = Solution()
print(so.minInteger(num = "4321", k = 4))
print(so.minInteger(num = "100", k = 1))
print(so.minInteger(num = "36789", k = 1000))
print(so.minInteger(num = "22", k = 22))
print(so.minInteger(num = "9438957234785635408", k = 23))





