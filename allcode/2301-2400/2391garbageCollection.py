# 给你一个下标从 0开始的字符串数组garbage，其中garbage[i]表示第 i个房子的垃圾集合。garbage[i]只包含字符'M'，'P' 和'G'，但可能包含多个相同字符，每个字符分别表示一单位的金属、纸和玻璃。垃圾车收拾 一单位的任何一种垃圾都需要花费1分钟。
#
# 同时给你一个下标从 0开始的整数数组travel，其中travel[i]是垃圾车从房子 i行驶到房子 i + 1需要的分钟数。
#
# 城市里总共有三辆垃圾车，分别收拾三种垃圾。每辆垃圾车都从房子 0出发，按顺序到达每一栋房子。但它们 不是必须到达所有的房子。
#
# 任何时刻只有 一辆垃圾车处在使用状态。当一辆垃圾车在行驶或者收拾垃圾的时候，另外两辆车 不能做任何事情。
#
# 请你返回收拾完所有垃圾需要花费的 最少总分钟数。
#
#
#
# 示例 1：
#
# 输入：garbage = ["G","P","GP","GG"], travel = [2,4,3]
# 输出：21
# 解释：
# 收拾纸的垃圾车：
# 1. 从房子 0 行驶到房子 1
# 2. 收拾房子 1 的纸垃圾
# 3. 从房子 1 行驶到房子 2
# 4. 收拾房子 2 的纸垃圾
# 收拾纸的垃圾车总共花费 8 分钟收拾完所有的纸垃圾。
# 收拾玻璃的垃圾车：
# 1. 收拾房子 0 的玻璃垃圾
# 2. 从房子 0 行驶到房子 1
# 3. 从房子 1 行驶到房子 2
# 4. 收拾房子 2 的玻璃垃圾
# 5. 从房子 2 行驶到房子 3
# 6. 收拾房子 3 的玻璃垃圾
# 收拾玻璃的垃圾车总共花费 13 分钟收拾完所有的玻璃垃圾。
# 由于没有金属垃圾，收拾金属的垃圾车不需要花费任何时间。
# 所以总共花费 8 + 13 = 21 分钟收拾完所有垃圾。
# 示例 2：
#
# 输入：garbage = ["MMM","PGM","GP"], travel = [3,10]
# 输出：37
# 解释：
# 收拾金属的垃圾车花费 7 分钟收拾完所有的金属垃圾。
# 收拾纸的垃圾车花费 15 分钟收拾完所有的纸垃圾。
# 收拾玻璃的垃圾车花费 15 分钟收拾完所有的玻璃垃圾。
# 总共花费 7 + 15 + 15 = 37 分钟收拾完所有的垃圾。
#
#
# 提示：
#
# 2 <= garbage.length <= 105
# garbage[i] 只包含字母'M'，'P'和'G'。
# 1 <= garbage[i].length <= 10
# travel.length == garbage.length - 1
# 1 <= travel[i] <= 100


from leetcode.allcode.competition.mypackage import *

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def helper(chr):
            tr = 0
            ans = garbage[0].count(chr)
            for i, gar in enumerate(garbage[1:]):
                tr += travel[i]
                if chr in gar:
                    ans += gar.count(chr)
                    ans += tr
                    tr = 0
            return ans
        ans = helper('P') + helper('M') + helper('G')
        return ans



so = Solution()
print(so.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
print(so.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))




