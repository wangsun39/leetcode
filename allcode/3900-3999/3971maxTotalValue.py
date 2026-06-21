# 给你两个整数数组 value 和 decay，以及一个整数 m。
#
# value[i] 表示下标 i 的初始价值。
# decay[i] 表示每次选择下标 i 后，该下标的价值会减少的数值。
# 你可以多次 选择 任意下标。所有下标的总选择次数不得超过 m。
#
# 如果重复选择下标 i，第 t 次（从 1 开始计数）获得的价值为 value[i] - decay[i] * (t - 1)。
#
# 返回你能够获得的 最大 总价值。由于答案可能很大，请返回其对 109 + 7 取模后的结果。
#
#
#
# 示例 1：
#
# 输入： value = [6,5,4], decay = [2,1,1], m = 4
#
# 输出： 19
#
# 解释：
#
# 一种最优选择序列如下：
#
# 选择下标 0，获得的价值为 6。
# 选择下标 1，获得的价值为 5。
# 选择下标 2，获得的价值为 4。
# 再次选择下标 0，获得的价值为 6 - 2 = 4。
# 总价值为 6 + 5 + 4 + 4 = 19。在至多 4 次选择中，没有其他选择序列能获得更高的总价值。
#
# 示例 2：
#
# 输入： value = [7,2,2], decay = [3,2,1], m = 2
#
# 输出： 11
#
# 解释：
#
# 一种最优选择序列如下：
#
# 选择下标 0，获得的价值为 7。
# 再次选择下标 0，获得的价值为 7 - 3 = 4。
# 总价值为 7 + 4 = 11。
#
# 示例 3：
#
# 输入： value = [4,3], decay = [5,4], m = 5
#
# 输出： 7
#
# 解释：
#
# 一种最优选择序列如下：
#
# 选择下标 0，获得的价值为 4。
# 选择下标 1，获得的价值为 3。
# 总价值为 4 + 3 = 7。
#
#
#
# 提示：
#
# 1 <= value.length == decay.length <= 105
# 1 <= value[i], decay[i] <= 109
# 1 <= m <= 109

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(value)
        mx = max(value)

        def check(val):
            s = 0
            for i in range(n):
                t = (value[i] + decay[i] - val) // decay[i]  # 最多选t个i
                t = MAX(t, 0)
                s += t
                if s > m:
                    return False
            return True

        if check(0):
            # 选择次数无限制
            upper = 0  # 对答案的贡献值中，最大能选的数字，通过二分获取
        else:
            lo, hi = 0, mx + 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid
            upper = hi


        # 按 upper 挑选所有i
        ans = 0
        hp = []
        for i in range(n):
            t = (value[i] + decay[i] - upper) // decay[i]
            if t > 0:
                ans += t * value[i] - decay[i] * (t - 1) * t // 2
                ans %= MOD
                value[i] -= decay[i] * t
                if value[i] > 0:
                    heappush(hp, [-value[i], i])
                m -= t
            else:
                if value[i] > 0:
                    heappush(hp, [-value[i], i])

        while m and hp:
            x, i = heappop(hp)
            ans += -x
            ans %= MOD
            if x > decay[i]:
                heappush(hp, [-(x - decay[i]), i])
            m -= 1

        return ans % MOD



so = Solution()
print(so.maxTotalValue(value = [8,6,8], decay = [1,3,5], m = 1))
print(so.maxTotalValue(value = [4,3], decay = [5,4], m = 5))
print(so.maxTotalValue(value = [6,5,4], decay = [2,1,1], m = 4))




