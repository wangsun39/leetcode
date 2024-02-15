# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
# 返回分配方案中尽可能 最小 的 最大工作时间 。
#
#
#
# 示例 1：
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
# 示例 2：
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
#
#
# 提示：
#
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 107

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        @cache
        def sjob(bits):  # 求和
            s = 0
            for i in range(n):
                if bits & (1 << i):
                    s += jobs[i]
            return s
        ss = [0] * (1 << n)
        for i in range(1 << n):
            ss[i] = sjob(i)
        def check(t):

            @cache
            def dfs(idx, bits):  # 从idx工人开始分配，未分配的工作占位是bits
                if k - idx > bits.bit_count():  # 当工人数比工作数多时，明显是不合理的分配，不需要进行下去了
                    return inf
                # print(idx, bits)
                if ss[bits] <= t:
                    return True
                if idx == k - 1:
                    return False
                sub = bits
                while sub:
                    # 处理 sub 的逻辑
                    if sub != bits:
                        if ss[sub ^ bits] <= t:
                            if dfs(idx + 1, sub):
                                return True
                    sub = (sub - 1) & bits

                return False
            return dfs(0, (1 << n) - 1)


        lo, hi = max(jobs) - 1, sum(jobs)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            # print(11)
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


so = Solution()
print(so.minimumTimeRequired([101,102,103,104,105,106,107,108,109,110,111,10000000], 11))
print(so.minimumTimeRequired([6518448,8819833,7991995,7454298,2087579,380625,4031400,2905811,4901241,8480231,7750692,3544254], 4))
print(so.minimumTimeRequired(jobs = [3,2,3], k = 3))
print(so.minimumTimeRequired(jobs = [1,2,4,7,8], k = 2))




