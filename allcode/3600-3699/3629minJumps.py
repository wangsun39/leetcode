# 给你一个整数数组 nums，其长度可以被 3 整除。
#
# 你需要通过多次操作将数组清空。在每一步操作中，你可以从数组中选择任意三个元素，计算它们的 中位数 ，并将这三个元素从数组中移除。
#
# 奇数长度数组的 中位数 定义为数组按非递减顺序排序后位于中间的元素。
#
# 返回通过所有操作得到的 中位数之和的最大值 。
#
#
#
# 示例 1：
#
# 输入： nums = [2,1,3,2,1,3]
#
# 输出： 5
#
# 解释：
#
# 第一步，选择下标为 2、4 和 5 的元素，它们的中位数是 3。移除这些元素后，nums 变为 [2, 1, 2]。
# 第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 2。移除这些元素后，nums 变为空数组。
# 因此，中位数之和为 3 + 2 = 5。
#
# 示例 2：
#
# 输入： nums = [1,1,10,10,10,10]
#
# 输出： 20
#
# 解释：
#
# 第一步，选择下标为 0、2 和 3 的元素，它们的中位数是 10。移除这些元素后，nums 变为 [1, 10, 10]。
# 第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 10。移除这些元素后，nums 变为空数组。
# 因此，中位数之和为 10 + 10 = 20。
#
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 105
# nums.length % 3 == 0
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

def all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    flg = False
    for i in range(2, n + 1):
        if not is_prime[i]: continue
        if flg:
            continue
        if i * i > n:
            flg = True
            continue
        j = i * i
        while j < n + 1:
            is_prime[j] = False
            j += i
    return is_prime

primes = all_primes(10 ** 6 + 1)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        p_next = defaultdict(list)  # 质数的相邻节点 (包括质数和非质数)
        for i, x in enumerate(nums):
            if primes[x]:
                p_next[x].append(i)
        @cache
        def prime_factors(x):
            res = []
            i = 2
            while i * i <= x:
                if x % i != 0:
                    i += 1
                    continue
                res.append(i)
                while x % i == 0:
                    x //= i
                i += 1
            if x > 1:
                res.append(x)
            return res

        for i, x in enumerate(nums):
            if not primes[x]:
                arr = prime_factors(x)
                for y in arr:
                    p_next[y].append(i)

        dist = [inf] * n
        dist[0] = 0
        h = [(0, 0)]
        p_vis = set()  # 记录哪些质数已经访问过
        while h:
            d, i = heappop(h)
            x = nums[i]
            cand = []
            if i - 1 >= 0 and dist[i - 1] == inf:
                cand.append(i - 1)
            if i + 1 < n and dist[i + 1] == inf:
                cand.append(i + 1)
            if x in p_next and x not in p_vis:
                cand += p_next[x]
                p_vis.add(x)

            for y in cand:
                new_d = dist[i] + 1
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))

        return dist[n - 1]


so = Solution()
print(so.minJumps(nums = [2,7,7]))
print(so.minJumps(nums = [1,2,4,6]))
print(so.minJumps(nums = [7,5,7]))
print(so.minJumps(nums = [4,5,2]))




