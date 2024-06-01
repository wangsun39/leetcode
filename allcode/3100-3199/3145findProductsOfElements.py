# 一个整数 x 的 强数组 指的是满足和为 x 的二的幂的最短有序数组。比方说，11 的强数组为 [1, 2, 8] 。
#
# 我们将每一个正整数 i （即1，2，3等等）的 强数组 连接得到数组 big_nums ，big_nums 开始部分为 [1, 2, 1, 2, 4, 1, 4, 2, 4, 1, 2, 4, 8, ...] 。
#
# 给你一个二维整数数组 queries ，其中 queries[i] = [fromi, toi, modi] ，你需要计算 (big_nums[fromi] * big_nums[fromi + 1] * ... * big_nums[toi]) % modi 。
#
# 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。
#
#
#
# 示例 1：
#
# 输入：queries = [[1,3,7]]
#
# 输出：[4]
# 
# 解释：
#
# 只有一个查询。
#
# big_nums[1..3] = [2,1,2] 。它们的乘积为 4 ，4 对 7 取余数得到 4 。
#
# 示例 2：
#
# 输入：queries = [[2,5,3],[7,7,4]]
#
# 输出：[2,2]
#
# 解释：
#
# 有两个查询。
#
# 第一个查询：big_nums[2..5] = [1,2,4,1] 。它们的乘积为 8 ，8 对 3 取余数得到 2 。
#
# 第二个查询：big_nums[7] = 2 ，2 对 4 取余数得到 2 。
#
#
#
# 提示：
#
# 1 <= queries.length <= 500
# queries[i].length == 3
# 0 <= queries[i][0] <= queries[i][1] <= 1015
# 1 <= queries[i][2] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:


so = Solution()




