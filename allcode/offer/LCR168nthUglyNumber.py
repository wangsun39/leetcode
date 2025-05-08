# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
# 说明：丑数是只包含质因数 2、3 和/或 5 的正整数；1 是丑数。
#
#
#
# 示例 1：
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 提示：
#
# 1 <= n <= 1690
#
#
# 注意：本题与主站 264 题相同： https://leetcode-cn.com/problems/ugly-number-ii/

from leetcode.allcode.competition.mypackage import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = [1]
        heapify(hp)
        x = 0
        vis = {1}
        for _ in range(n):
            x = heappop(hp)
            if x * 2 not in vis:
                heappush(hp, x * 2)
                vis.add(x * 2)
            if x * 3 not in vis:
                heappush(hp, x * 3)
                vis.add(x * 3)
            if x * 5 not in vis:
                heappush(hp, x * 5)
                vis.add(x * 5)
        return x



