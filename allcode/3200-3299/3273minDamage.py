# 给你一个整数 power 和两个整数数组 damage 和 health ，两个数组的长度都为 n 。
#
# Bob 有 n 个敌人，如果第 i 个敌人还活着（也就是健康值 health[i] > 0 的时候），每秒钟会对 Bob 造成 damage[i] 点 伤害。
#
# 每一秒中，在敌人对 Bob 造成伤害 之后 ，Bob 会选择 一个 还活着的敌人进行攻击，该敌人的健康值减少 power 。
#
# 请你返回 Bob 将 所有 n 个敌人都消灭之前，最少 会受到多少伤害。
#
#
#
# 示例 1：
#
# 输入：power = 4, damage = [1,2,3,4], health = [4,5,6,8]
#
# 输出：39
#
# 解释：
#
# 最开始 2 秒内都攻击敌人 3 ，然后敌人 3 会被消灭，这段时间内对 Bob 的总伤害是 10 + 10 = 20 点。
# 接下来 2 秒内都攻击敌人 2 ，然后敌人 2 会被消灭，这段时间内对 Bob 的总伤害是 6 + 6 = 12 点。
# 接下来 1 秒内都攻击敌人 0 ，然后敌人 0 会被消灭，这段时间内对 Bob 的总伤害是 3 点。
# 接下来 2 秒内都攻击敌人 1 ，然后敌人 1 会被消灭，这段时间内对 Bob 的总伤害是 2 + 2 = 4 点。
# 示例 2：
#
# 输入：power = 1, damage = [1,1,1,1], health = [1,2,3,4]
#
# 输出：20
#
# 解释：
#
# 最开始 1 秒内都攻击敌人 0 ，然后敌人 0 会被消灭，这段时间对 Bob 的总伤害是 4 点。
# 接下来 2 秒内都攻击敌人 1 ，然后敌人 1 会被消灭，这段时间对 Bob 的总伤害是 3 + 3 = 6 点。
# 接下来 3 秒内都攻击敌人 2 ，然后敌人 2 会被消灭，这段时间对 Bob 的总伤害是 2 + 2 + 2 = 6 点。
# 接下来 4 秒内都攻击敌人 3 ，然后敌人 3 会被消灭，这段时间对 Bob 的总伤害是 1 + 1 + 1 + 1 = 4 点。
# 示例 3：
#
# 输入：power = 8, damage = [40], health = [59]
#
# 输出：320
#
#
#
# 提示：
#
# 1 <= power <= 104
# 1 <= n == damage.length == health.length <= 105
# 1 <= damage[i], health[i] <= 104


from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        def cmp(t1, t2):
            # 比较决定t1, t2两个任务哪个先执行，就看不同的顺序哪个伤害更大
            d1, h1 = t1
            d2, h2 = t2
            v1 = (h1 + power - 1) // power * d2  # 先消灭1，再消灭2
            v2 = (h2 + power - 1) // power * d1  # 先消灭2，再消灭1
            if v1 > v2:
                return v1
            if v1 < v2:
                return -1
            return 0
        arr = list(zip(damage, health))
        arr.sort(key=cmp_to_key(cmp))
        ans = seconds = 0
        for d, h in arr:
            ans += seconds * d
            t = (h + power - 1) // power
            ans += t * d
            seconds += t
        return ans


so = Solution()
print(so.minDamage(power = 4, damage = [1,2,3,4], health = [4,5,6,8]))
print(so.minDamage(power = 1, damage = [1,1,1,1], health = [1,2,3,4]))
print(so.minDamage(power = 8, damage = [40], health = [59]))




