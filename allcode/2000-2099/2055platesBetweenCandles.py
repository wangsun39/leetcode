# 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0开始的字符串s，它只包含字符'*' 和'|'，其中'*'表示一个 盘子，'|'表示一支蜡烛。
#
# 同时给你一个下标从 0开始的二维整数数组queries，其中queries[i] = [lefti, righti]表示 子字符串s[lefti...righti]（包含左右端点的字符）。对于每个查询，你需要找到 子字符串中在 两支蜡烛之间的盘子的 数目。如果一个盘子在 子字符串中左边和右边 都至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间。
#
# 比方说，s = "||**||**|*"，查询[3, 8]，表示的是子字符串"*||**|"。子字符串中在两支蜡烛之间的盘子数目为2，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
# 请你返回一个整数数组answer，其中answer[i]是第i个查询的答案。
#
# 
#
# 示例 1:
#
#
#
# 输入：s = "**|**|***|", queries = [[2,5],[5,9]]
# 输出：[2,3]
# 解释：
# - queries[0] 有两个盘子在蜡烛之间。
# - queries[1] 有三个盘子在蜡烛之间。
# 示例 2:
#
#
#
# 输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# 输出：[9,0,0,0,0]
# 解释：
# - queries[0] 有 9 个盘子在蜡烛之间。
# - 另一个查询没有盘子在蜡烛之间。
# 
#
# 提示：
#
# 3 <= s.length <= 105
# s只包含字符'*' 和'|'。
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= lefti <= righti < s.length



from leetcode.allcode.competition.mypackage import *

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        posOfClosest = {} # 记录左右两边最近的蜡烛的下标
        numOfLeftPlates = {}  # 记录左边盘子总数
        N = len(s)
        pos = -1
        num = 0
        for i in range(N):
            if s[i] == '|':
                pos = i
                numOfLeftPlates[i] = num
            else:
                posOfClosest[i] = [pos, -1]
                num += 1
        for i in range(N-1, -1, -1):
            if s[i] == '|':
                pos = i
            else:
                posOfClosest[i][1] = pos
        print(numOfLeftPlates)
        print(posOfClosest)
        def find(query):
            if query[0] in posOfClosest:
                left = posOfClosest[query[0]][1]
                if left == -1 or left >= query[1] - 1:
                    return 0
            else:
                left = query[0]
            if query[1] in posOfClosest:
                right = posOfClosest[query[1]][0]
                if right == -1 or right <= query[0] + 1:
                    return 0
            else:
                right = query[1]
            return numOfLeftPlates[right] - numOfLeftPlates[left]
        res = []
        for query in queries:
            res.append(find(query))

        return res





so = Solution()
print(so.platesBetweenCandles("**|**|***|", queries = [[2,5],[5,9]]))
print(so.platesBetweenCandles("***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))

