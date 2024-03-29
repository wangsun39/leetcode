# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
#
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。
#
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
#
#
# 示例 1：
#
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
#  数字     成本
#   1  ->   4
#   2  ->   3
#   3  ->   2
#   4  ->   5
#   5  ->   6
#   6  ->   7
#   7  ->   2
#   8  ->   5
#   9  ->   5
# 示例 2：
#
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
# 示例 3：
#
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
# 示例 4：
#
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
#
#
# 提示：
#
# cost.length == 9
# 1 <= cost[i] <= 5000
# 1 <= target <= 5000



from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestNumber1(self, cost: List[int], target: int) -> str:
        def MAX(a, b):
            sa, sb = sum(a), sum(b)
            if sa == sb:
                return a if a > b else b
            return a if sa > sb else b

        s = set()  # 这是个小优化，效果不明显
        for i in range(8, -1, -1):
            if cost[i] in s:
                cost[i] = 0
            else:
                s.add(cost[i])
        dp1 = [[-1] * 9 for _ in range(target + 1)]  # dp1[j] 表示前i个数组成目标为j的组大数字组合，这个组合是个9个元素的list，表示1-9这9个数的数量（倒序放置便于排序）
        dp1[0] = [0] * 9
        dp2 = [0] * (target + 1)
        for i in range(9):
            if cost[i] == 0: continue
            for j in range(target + 1):
                dp2[j] = dp1[j][:]
                if j >= cost[i]:
                    tmp = dp2[j - cost[i]][:]
                    if tmp[8 - i] >= 0:
                        tmp[8 - i] += 1
                        dp2[j] = MAX(dp2[j], tmp)[:]
            dp1, dp2 = dp2, [0] * (target + 1)

        # print(dp1[-1])
        if dp1[-1][0] == -1: return '0'
        ans = ''
        for i, x in enumerate(dp1[-1]):
            ans += str(9 - i) * x
        return ans

    def largestNumber(self, cost: List[int], target: int) -> str:
        s = set()
        for i in range(8, -1, -1):
            if cost[i] not in s:
                s.add(cost[i])
            else:
                cost[i] = 10000  # 相同cost元素，只保留大的数
        def MAX(a, b):
            if len(a) > len(b):
                return a
            elif len(a) < len(b):
                return b
            return max(a, b)

        @cache
        def dfs(start, t):
            if t == 0: return ''
            if start == 0:
                if t % cost[start] == 0:
                    return '1' * (t // cost[start])
                else:
                    return None
            res = ''
            i = 0
            while cost[start] * i <= t:
                ret = dfs(start - 1, t - cost[start] * i)
                if ret is not None:
                    res = MAX(res, str(start + 1) * i + ret)
                i += 1
            return None if res == '' else res

        ans = dfs(8, target)
        return '0' if ans is None else ans





so = Solution()
print(so.largestNumber(cost = [1,1,1,1,1,1,1,1,1], target = 5000))
print(so.largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9))  # 7772
print(so.largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5))  # 0
print(so.largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12))   # 85
print(so.largestNumber(cost = [6,10,15,40,40,40,40,40,40], target = 47))  # "32211"




