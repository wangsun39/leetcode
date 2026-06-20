# 各位勇者请注意，力扣太空城发布陨石雨红色预警。
#
# 太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 0 ~ N 的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下：
#
# 选择一个舱室开启屏障，能量消耗为 2
# 选择相邻两个舱室开启联合屏障，能量消耗为 3
# 对于已开启的一个屏障，多维持一时刻，能量消耗为 1
# 已知陨石雨的影响范围和到达时刻，time[i] 和 position[i] 分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的最少能量。
#
# 注意：
#
# 同一时间，一个舱室不能被多个屏障覆盖
# 陨石雨仅在到达时刻对冲击位置处的舱室有影响
# 示例 1：
#
# 输入：time = [1,2,1], position = [6,3,3]
#
# 输出：5
#
# 解释： 时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4 时刻 2，维持编号 3 舱室的屏障，能量消耗 1 因此，最少需要能量 5
#
# 示例 2：
#
# 输入：time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]
#
# 输出：9
#
# 解释： 时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3 时刻 1，开启编号 3 舱室的屏障，能量消耗 2 时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1 时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1 时刻 5，重新开启编号 3 舱室的联合屏障，能量消耗 2 因此，最少需要能量 9
#
# 提示：
#
# 1 <= time.length == position.length <= 500
# 1 <= time[i] <= 5
# 0 <= position[i] <= 100

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
        m, n = max(time), max(position) + 1

        time_mask = [0] * n  # 每个位置需要屏障的所有时间点掩码
        for t, p in zip(time, position):
            time_mask[p] |= 1 << (t - 1)

        ns = 1 << m  # 时间的子集数量
        all_masks = ns - 1
        dp = [[inf] * ns for _ in range(n)]   # dp[i][j] 表示 前i个位置处理结束，且第i个位置开启向后的联合屏障的时间点子集为j时，消耗的最小能量
        for i in range(n):
            for j in range(ns):

                # 能转移过来的子集只有与 j的交集是空的状态sub，因为不能同时在i和i-1都使用联合屏障，其他情况都有可能
                mj = all_masks ^ j  # 能取的所有时间点，枚举mj的每个子集就是sub， 即i-1上的时间点状态
                sub = mj
                while True:
                    # 处理 sub 的逻辑
                    res = 0
                    if i:
                        res = dp[i - 1][sub]  # 从i-1转移过来的能量
                    uncover = time_mask[i] & ~(j | sub)  # 位置i未被联合屏障覆盖，且需要设置屏障的时间点
                    if 1 & j:  # 第一个屏障用联合屏障
                        res += 3
                    elif 1 & uncover:  # 第一个屏障用普通屏障
                        res += 2
                    for k in range(1, m):  # 遍历时间
                        if (1 << k) & j:
                            if (1 << (k - 1)) & j:  # 维持屏障
                                res += 1
                            else:
                                res += 3
                        elif (1 << k) & uncover:
                            if (1 << (k - 1)) & uncover:  # 维持屏障
                                res += 1
                            else:
                                res += 2
                    dp[i][j] = MIN(dp[i][j], res)

                    sub = (sub - 1) & mj
                    if sub == mj:
                        break
        return min(dp[-1])



so = Solution()
print(so.defendSpaceCity(time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]))  # 9
print(so.defendSpaceCity(time = [1,2,1], position = [6,3,3]))  # 5

