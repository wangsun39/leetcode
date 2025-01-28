# f(x)是x!末尾是 0 的数量。回想一下x! = 1 * 2 * 3 * ... * x，且 0! = 1。
#
# 例如，f(3) = 0，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2，因为 11!= 39916800 末端有 2 个 0 。
# 给定k，找出返回能满足 f(x) = k的非负整数 x的数量。
#
#
#
# 示例 1：
#
# 输入：k = 0
# 输出：5
# 解释：0!, 1!, 2!, 3!, 和 4!均符合 k = 0 的条件。
# 示例 2：
#
# 输入：k = 5
# 输出：0
# 解释：没有匹配到这样的 x!，符合 k = 5 的条件。
# 示例 3:
#
# 输入: k = 3
# 输出: 5
#
#
# 提示:
#
# 0 <= k <= 109



from typing import List

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        base = [5 ** i for i in range(1, 16)]
        def helper(n):
            i, ans = 0, 0
            while n >= base[i]:
                ans += (n // base[i])
                i += 1
            return ans

        def bisect_left(x, key):
            lo, hi = 0, int(1e10)
            while lo < hi:
                mid = (lo + hi) // 2
                if key(mid) < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def bisect_right(x, key=None):
            lo, hi = 0, int(1e10)
            while lo < hi:
                mid = (lo + hi) // 2
                if x < key(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        # print(helper(5))
        p1, p2 = bisect_left(k, helper), bisect_left(k + 1, helper)
        if helper(p1) != k:
            return 0
        return p2 - p1


so = Solution()
print(so.preimageSizeFZF(0))
print(so.preimageSizeFZF(5))
print(so.preimageSizeFZF(3))

