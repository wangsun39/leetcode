# 给你一个整数数组 nums 。请你对数组执行下述操作：
#
# 从 nums 中找出 任意 两个 相邻 的 非互质 数。
# 如果不存在这样的数，终止 这一过程。
# 否则，删除这两个数，并 替换 为它们的 最小公倍数（Least Common Multiple，LCM）。
# 只要还能找出两个相邻的非互质数就继续 重复 这一过程。
# 返回修改后得到的 最终 数组。可以证明的是，以 任意 顺序替换相邻的非互质数都可以得到相同的结果。
#
# 生成的测试用例可以保证最终数组中的值 小于或者等于 108 。
#
# 两个数字 x 和 y 满足 非互质数 的条件是：GCD(x, y) > 1 ，其中 GCD(x, y) 是 x 和 y 的 最大公约数 。
#
#
#
# 示例 1 ：
#
# 输入：nums = [6,4,3,2,7,6,2]
# 输出：[12,7,6]
# 解释：
# - (6, 4) 是一组非互质数，且 LCM(6, 4) = 12 。得到 nums = [12,3,2,7,6,2] 。
# - (12, 3) 是一组非互质数，且 LCM(12, 3) = 12 。得到 nums = [12,2,7,6,2] 。
# - (12, 2) 是一组非互质数，且 LCM(12, 2) = 12 。得到 nums = [12,7,6,2] 。
# - (6, 2) 是一组非互质数，且 LCM(6, 2) = 6 。得到 nums = [12,7,6] 。
# 现在，nums 中不存在相邻的非互质数。
# 因此，修改后得到的最终数组是 [12,7,6] 。
# 注意，存在其他方法可以获得相同的最终数组。
# 示例 2 ：
#
# 输入：nums = [2,2,1,1,3,3,3]
# 输出：[2,1,1,3]
# 解释：
# - (3, 3) 是一组非互质数，且 LCM(3, 3) = 3 。得到 nums = [2,2,1,1,3,3] 。
# - (3, 3) 是一组非互质数，且 LCM(3, 3) = 3 。得到 nums = [2,2,1,1,3] 。
# - (2, 2) 是一组非互质数，且 LCM(2, 2) = 2 。得到 nums = [2,1,1,3] 。
# 现在，nums 中不存在相邻的非互质数。
# 因此，修改后得到的最终数组是 [2,1,1,3] 。
# 注意，存在其他方法可以获得相同的最终数组。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 生成的测试用例可以保证最终数组中的值 小于或者等于 108 。
import math

from leetcode.allcode.competition.mypackage import *


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def dfs(arr):
            n = len(arr)
            if n <= 1: return arr
            mid = n // 2
            l = dfs(arr[:mid])
            r = dfs(arr[mid:])
            ll, lr = len(l), len(r)
            if ll == 0 or lr == 0 or math.gcd(l[-1], r[0]) == 1:
                return l + r
            cur = math.lcm(l[-1], r[0])
            lp, rp = ll - 2, 1
            while (lp >= 0 and math.gcd(l[lp], cur) > 1) or (rp < lr and math.gcd(r[rp], cur) > 1):
                if lp >= 0 and math.gcd(l[lp], cur) > 1:
                    cur = math.lcm(cur, l[lp])
                    lp -= 1
                if rp < lr and math.gcd(r[rp], cur) > 1:
                    cur = math.lcm(cur, r[rp])
                    rp += 1
            res = []
            if lp >= 0:
                res += l[:lp + 1]
            res += [cur]
            if rp < lr:
                res += r[rp:]
            return res
        return dfs(nums)




so = Solution()
print(so.replaceNonCoprimes([57182,2,2,4,2,57182,28591,28591,57182,2,57182,2,2,2,57182,87,2523,3,3,8091,31,29,83607,1369,1369,1369,1369,1369,37,1369,1369,1369,37,37,1369,1369,37,37,1369,1369,1369,37,1369,1369,1369,1369,37,1369,37,1369,1369,37,1369,37,1369,37,37,37,37,1369,37,1369,37,37,1369,37,1369,1369,1369,1369,37,37,1369,1369,37,1369,1369,1369,37,37,37,1369,37,1369,1369,37,37,1369,1369,1369,37,1369,37,37,1369,37,1369,37,37,1369,37,37,37,1369,37,37,37,37,1369,37,1369,37,1369,37,37,37,37,1369,37,37,37,1369,37,1369,1369,37,37,1369,1369,37,37,1369,1369,1369,1369,37,1369,37,1369,37,1369,37,37,1369,37,1369,37,37,1369,1369,37,37,1369,37,37,37,1369,1369,37,37,37,37,37,1369,37,37,1369,37,1369,1369,1369,1369,37,1369,37,37,1369,37,37,37,1369,37,1369,37,37,1369,37,1369,37,1369,1369,37,37,37,1369,37,1369,37,1369,1369,1369,1369,37,37,37,37,37,1369,37,37,37,37,37,37,37,37,37,1369,1369,37,1369,37,37,37,37,37,1369,1369,1369,37,37,1369,37,37,37,1369,1369,37,1369,1369,1369,37,37,37,37,1369,1369,1369,1369,37,37,1369,1369,37,1369,1369,1369,37,1369,37,1369,1369,37,1369,37,37,1369,1369,37,37,37,37,37,1369,1369,37,1369,37,37,1369,1369,1369,1369,37,1369,37,1369,1369,37,1369,37,1369,1369,1369,1369,37,1369,1369,37,1369,1369,1369,37,1369,1369,37,1369,1369,37,37,1369,1369,1369,1369,1369,1369,1369,37,1369,1369,1369,1369,1369,37,1369,1369,1369,1369,1369,1369,37,1369,37,1369,37,37,37,1369,37,37,1369,1369,1369,1369,37,37,37,1369,1369,1369,37,37,37,1369,1369,37,37,37,1369,1369,37,1369,37,37,37,1369,1369,37,37,1369,37,1369,37,37,37,37,37,1369,37,37,37,37,37,1369,5,5,5,5,5,5,5,5,5,5,5,5,5,37,37,37,37,289,17,21386,34,2,34,2738,1258,2,34,46546,46546,34,2516,7,7,49,7,245,25,175,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767,72767]))
print(so.replaceNonCoprimes([6,4,3,2,7,6,2]))
print(so.replaceNonCoprimes(nums = [2,2,1,1,3,3,3]))