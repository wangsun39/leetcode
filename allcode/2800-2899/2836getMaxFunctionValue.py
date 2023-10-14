# 给你一个长度为 n 下标从 0 开始的整数数组 receiver 和一个整数 k 。
#
# 总共有 n 名玩家，玩家 编号 互不相同，且为 [0, n - 1] 中的整数。这些玩家玩一个传球游戏，receiver[i] 表示编号为 i 的玩家会传球给编号为 receiver[i] 的玩家。玩家可以传球给自己，也就是说 receiver[i] 可能等于 i 。
#
# 你需要从 n 名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 恰好 k 次。
#
# 如果选择编号为 x 的玩家作为开始玩家，定义函数 f(x) 表示从编号为 x 的玩家开始，k 次传球内所有接触过球玩家的编号之 和 ，如果有玩家多次触球，则 累加多次 。换句话说， f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver(k)[x] 。
#
# 你的任务时选择开始玩家 x ，目的是 最大化 f(x) 。
#
# 请你返回函数的 最大值 。
#
# 注意：receiver 可能含有重复元素。
#
#
#
# 示例 1：
#
# 传递次数	传球者编号	接球者编号	x + 所有接球者编号
#  	 	 	2
# 1	2	1	3
# 2	1	0	3
# 3	0	2	5
# 4	2	1	6
#
#
# 输入：receiver = [2,0,1], k = 4
# 输出：6
# 解释：上表展示了从编号为 x = 2 开始的游戏过程。
# 从表中可知，f(2) 等于 6 。
# 6 是能得到最大的函数值。
# 所以输出为 6 。
# 示例 2：
#
# 传递次数	传球者编号	接球者编号	x + 所有接球者编号
#  	 	 	4
# 1	4	3	7
# 2	3	2	9
# 3	2	1	10
#
#
# 输入：receiver = [1,1,1,2,3], k = 3
# 输出：10
# 解释：上表展示了从编号为 x = 4 开始的游戏过程。
# 从表中可知，f(4) 等于 10 。
# 10 是能得到最大的函数值。
# 所以输出为 10 。
#
#
# 提示：
#
# 1 <= receiver.length == n <= 105
# 0 <= receiver[i] <= n - 1
# 1 <= k <= 1010

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        M = 36
        n = len(receiver)
        nt1 = [[0] * M for _ in range(n)]  # nt[i][j]  记录第 i 个玩家 传球 2 ** j 次后的玩家
        nt2 = [[0] * M for _ in range(n)]  # nt[i][j]  记录第 i 个玩家 传球 2 ** j 次经过的玩家之和 （不包括起点）
        for i in range(n):
            nt1[i][0] = receiver[i]
            nt2[i][0] = receiver[i]
        for j in range(1, M):
            for i in range(n):
                v = nt1[i][j - 1]
                nt1[i][j] = nt1[v][j - 1]
                nt2[i][j] += (nt2[i][j - 1] + nt2[v][j - 1])
        def f(start):
            idx = 0
            cur = start
            kk = k
            ans = start
            while kk:
                if kk & 1:
                    ans += nt2[cur][idx]
                    cur = nt1[cur][idx]
                kk >>= 1
                idx += 1
            return ans
        return max(f(x) for x in range(n))



so = Solution()
print(so.getMaxFunctionValue(receiver = [0], k = 10000000000))
print(so.getMaxFunctionValue(receiver = [1,1,1,2,3], k = 4))
print(so.getMaxFunctionValue(receiver = [1,1,1,2,3], k = 3))
print(so.getMaxFunctionValue(receiver = [2,0,1], k = 4))




